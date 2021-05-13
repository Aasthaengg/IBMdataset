#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    children=[]
    n,x = map(int,input().split())
    children=list(map(int,input().split()))
    sorted_chiledren=sorted(children)
    counter=0
    last=x

    if sum(children) == x:
        print(n)
        exit()
    elif min(children) > x:
        print(0)
        exit()

    for idx,data in enumerate(sorted_chiledren):
        if data < last:
            last-=data
            counter+=1
            if idx+1==n:
                print(counter-1)
                exit()
        elif data == last:
            counter+=1
            print(counter)
            exit()
        else:
            print(counter)
            break

    
if __name__=="__main__":
    main()