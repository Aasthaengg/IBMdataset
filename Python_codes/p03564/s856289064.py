#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    K=I()
    ans=1
    for i in range(N):
        if ans<K:
            ans*=2
        else:
            ans+=K
    print(ans)
        

main()
