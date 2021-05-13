#-*-coding:utf-8-*-
import sys
import math
input=sys.stdin.readline

def main():
    maps=[]
    n = int(input())
    maps=list(map(int,input().split()))
    ans=0
    answers=[]

    for i in range(1,101):
        for data in maps:
            ans+=abs(i-data)**2
        answers.append(ans)
        ans=0
    print(min(answers))

if __name__=="__main__":
    main()