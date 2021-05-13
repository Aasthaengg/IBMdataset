import sys
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

from collections import deque

def main():
	m,k=MI()
	A=[]
	if k==0:
		for i in range(2**m):
			A.append(i)
			A.append(i)
		print(*A)
		exit()

	if 2**(m)<=k:
		print(-1)
		exit()

	if m==k==1:
		print(-1)
		exit()

	A.append(0)
	A.append(k)
	A.append(0)

	for i in range(1,2**m):
		if i!=k:
			A.append(i)
	A.append(k)

	for i in reversed(range(1,2**m)):
		if i!=k:
			A.append(i)

	print(*A)


















if __name__ == "__main__":
	main()
