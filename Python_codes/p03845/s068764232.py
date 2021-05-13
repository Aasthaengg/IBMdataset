#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import copy

def main():
    questions=[]
    dp=[]
    n = int(input())
    questions=list(map(int,input().split()))
    m = int(input())
    drinks=[list(map(int,input().split())) for _ in range(m)]
    for drink in drinks:
        dp=copy.deepcopy(questions)
        dp[drink[0]-1]=drink[1]
        print(sum(dp))
    
if __name__=="__main__":
    main()