#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    number = int(input())
    counter=[]
    count=0

    if number==1:
        print(1)
        exit()

    for i in range(1,number+1):
        while i >= 2:
            if i % 2==0:
                i /= 2
                count+=1
            else:
                break
        counter.append(count)
        count=0
    print(counter.index(max(counter))+1)

if __name__=="__main__":
    main()