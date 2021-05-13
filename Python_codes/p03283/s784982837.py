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
# rstrip().decode('utf-8')

#006
import numpy as np

def main():
	n,m,q=MI()
	li=np.zeros((n+1,n+1),dtype=np.int64)
	for _ in range(m):
		l,r=MI()
		li[l][r]+=1
	#print(li)

	li=np.cumsum(li,axis=0)
	li=np.cumsum(li,axis=1)
	#print(li)

	for _ in range(q):
		p,q=MI()
		print(li[q,q]-li[p-1,q]-li[q,p-1]+li[p-1,p-1])

if __name__ == "__main__":
	main()