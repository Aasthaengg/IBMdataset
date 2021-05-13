#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    n = list(map(int,input().rstrip()))
    digit=len(n)
    ans1=0
    ans2=0

    if digit==1:
        print(n[0])
        exit()
    else:
        ans1=sum(n)
        ans2=n[0]-1+(digit-1)*9
        print(max(ans1,ans2))

if __name__=="__main__":
    main()