#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    q,h,s,d = map(int,input().split())
    n = int(input())
    q=4*q
    h=2*h
    sp1=min(q,h,s)
    dp2=min(2*q,2*h,2*s,d)

    if n%2==0:
        c=n//2
        print(c*dp2)
    elif n%2!=0:
        c=n//2
        print(c*dp2+sp1)
    else:
        print(n*sp1)
    

if __name__=="__main__":
    main()