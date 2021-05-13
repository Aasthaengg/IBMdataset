import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
input = sys.stdin.buffer.readline


#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

import numpy as np

def main():
	n,s=MI()
	A=LI()

	li=[0]*(3010)
	li=np.array(li)
	li[0]=1
	#print(li)

	for i in A:
		tmp=li.copy()
		li*=2
		li[i:]+=tmp[:3010-i]
		li%=998244353
		#print(li)
	print(li[s])



if __name__ == "__main__":
	main()
