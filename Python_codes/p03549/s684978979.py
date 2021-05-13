#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    A=1900*M+100*(N-M)
    rep=pow(2,M)
    print(A*rep)

main()
