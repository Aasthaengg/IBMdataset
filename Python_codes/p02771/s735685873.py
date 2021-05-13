import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    A,B,C = LI()
    print("Yes" if ((A==B and B!=C) or (B==C and C!=A) or (C==A and A!=B)) else "No")

main()

