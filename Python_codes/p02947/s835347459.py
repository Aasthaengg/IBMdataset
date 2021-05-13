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

from collections import defaultdict

def main():
	n=II()
	d=defaultdict(int)
	for _ in range(n):
		s=list(RD())
		s.sort()
		d[tuple(s)]+=1

	ans=0

	for _,v in d.items():
		ans+=(v*(v-1))//2
	print(ans)









if __name__ == "__main__":
	main()
