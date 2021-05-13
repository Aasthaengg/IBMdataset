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
	k,n=MI()
	A=LI()
	A=np.array(A)
	A=np.append(A,A+k)

	B=A[n-1:]-A[:n+1]
	print(min(B))
















if __name__ == "__main__":
	main()
