#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    numbers=[]
    a,b = map(int,input().split())
    numbers=list(range(a,b+1))
    count=0

    for number in numbers:
        if str(number)[0]==str(number)[-1] and str(number)[1]== str(number)[3]:
            count+=1
    print(count)

if __name__=="__main__":
    main()