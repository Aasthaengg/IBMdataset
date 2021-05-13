#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    n = int(input())
    ans=10**12
    for a in range(1,10**6+1):
        if n%a==0:
            b=n//a
        ans=min(ans,a+b-2)
    print(ans)

if __name__=="__main__":
    main()