#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    l=LI()
    l.sort(reverse=True)
    ans=sum(l[:K])
    print(ans)

main()

