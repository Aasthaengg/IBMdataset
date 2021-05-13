#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))



        

def main():
    mod=10**9+7
    K=I()
    if K<=pow(10,16):
        N=2
        if K%2==0:
            ans=[K//2+1,K//2+1]
        else:
            ans=[K//2,K//2+3]
    else:
        N=50
        a=N-1+K//N
        b=K%N
        if b!=0:
            a-=b
        ans=[a]*N
        for i in range(b):
            ans[i]+=N+1
    
        
    print(N)
    print(' '.join(map(str, ans)))
    

        

main()
