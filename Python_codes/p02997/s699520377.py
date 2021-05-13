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
    N,K=map(int,input().split())
    if (N-1)*(N-2)//2<K:
        print(-1)
    else:
        ans=[]
        for i in range(2,N+1):
            ans.append((1,i))
        i,j=2,3
        for _ in range((N-1)*(N-2)//2-K):
            ans.append((i,j))
            j+=1
            if j>N:
                i+=1
                j=i+1
        print(len(ans))
        for a in ans:
            print(*a)

if __name__ == '__main__':
    main()
