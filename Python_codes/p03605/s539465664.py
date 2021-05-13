#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    if N%10==9 or N//10==9:
        print("Yes")
    else:
        print("No")

main()
