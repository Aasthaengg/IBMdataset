#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    A,B=MI()
    if A%3==0 or B%3==0 or(A+B)%3==0:
        print("Possible")
    else:
        print("Impossible")
        

main()

