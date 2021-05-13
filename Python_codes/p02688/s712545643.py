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
	n,k=MI()
	s=set()
	for _ in range(k):
		d=II()
		A=set(LI())
		s|=(A)
	print(n-len(s))
	
	









if __name__=="__main__":
	main()
