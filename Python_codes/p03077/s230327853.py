import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

import numpy as np

def main():
	n=II()
	A=[II() for _ in range(5)]
	ans=0

	for i in A:
		ans=max(ans,(n-1)//i)

	ans+=5

	print(ans)









if __name__ == "__main__":
	main()
