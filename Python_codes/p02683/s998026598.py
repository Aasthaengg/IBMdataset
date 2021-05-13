import sys

input=sys.stdin.buffer.readline


#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()


def II(): return int(input())


def MI(): return map(int,input().split())


def MF(): return map(float,input().split())


def LI(): return list(map(int,input().split()))


def LF(): return list(map(float,input().split()))


def TI(): return tuple(map(int,input().split()))


# rstrip().decode('utf-8')

import numpy as np

def main():
	n,m,x=MI()
	C=[]
	A=[]
	for _ in range(n):
		c_,*A_=LI()
		C.append(c_)
		A.append(A_)
	A=np.array(A)
	
	ans=10**10
	
	for i in range(1<<n):
		B=np.zeros(m)
		cnt=0
		for j in range(n):
			if 1<<j&i:
				cnt+=C[j]
				B+=A[j]
		if np.min(B)>=x:
			ans=min(ans,cnt)
	print(ans if ans!=10**10 else -1)
	





if __name__=="__main__":
	main()
