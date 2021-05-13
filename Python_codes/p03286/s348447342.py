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
    l=[(-2)**i for i in range(32)]
    S=[0]*34
    for i in range(16):
        S[i*2+2]=S[i*2]+l[i*2]
        S[i*2+3]=S[i*2+1]+l[i*2+1]
    ans=0
    while N!=0:
        for i in range(16):
            if abs(S[i*2+2+(N<0)])>=abs(N):
                ans|=1<<(i*2+(N<0))
                N-=l[i*2+(N<0)]
                break
    print(format(ans,'b'))

if __name__ == '__main__':
    main()
