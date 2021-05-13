import sys
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
	a,b,c,d=MI()
	c-=a
	d-=b
	
	s="URDLLURDRDLU"
	li=[d,c,d,c,1,d+1,c+1,1,1,d+1,c+1,1]
	
	t=""
	for i in range(len(s)):
		t+=s[i]*li[i]
	print(t)
	




	

if __name__=="__main__":
	main()
