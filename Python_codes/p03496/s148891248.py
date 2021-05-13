# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N=int(input())
    a=tuple(map(int,input().split()))
    MAX=max(a)
    MIN=min(a)
    MAX_i=a.index(MAX)
    MIN_i=a.index(MIN)
    ans=[]
    if MAX>abs(MIN):
        for i in range(N):
            if i==MAX_i:
                continue
            ans.append((MAX_i,i))
        for i in range(N-1):
            ans.append((i,i+1))
    else:
        for i in range(N):
            if i==MIN_i:
                continue
            ans.append((MIN_i,i))
        for i in range(N-1,0,-1):
            ans.append((i,i-1))
    print(len(ans))
    for a in ans:
        print(a[0]+1,a[1]+1)

if __name__ == '__main__':
    main()
