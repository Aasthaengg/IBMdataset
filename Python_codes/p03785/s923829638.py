import sys
read = sys.stdin.buffer.read
#input = sys.stdin.readline
#input = sys.stdin.buffer.readline

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
from math import *


def main():
	n,c,k=MI()
	T=[II() for _ in range(n)]
	T.sort()
	#print(T)
	
	ans=0
	cnt=0
	now=0
	
	i=0
	
	while i<n:
		#print(i)
		now=T[i]
		ans+=1
		cnt=1
		while i<n and cnt<=c and now+k>=T[i]:
			i+=1
			cnt+=1
		cnt=0
	
	print(ans)
	
	
	
	
	


	
if __name__ == "__main__":
	main()
