import sys
input = sys.stdin.readline().rstrip
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
# rstrip().decode()

#import numpy as np


def main():
	s=input()
	#print(s)

	n=len(s)

	l=0
	r=n-1

	ans=0

	while l<r:

		if s[l]==s[r]:
			l+=1
			r-=1

		elif s[l]=="x":
			ans+=1
			l+=1

		elif s[r]=="x":
			ans+=1
			r-=1

		else:
			print(-1)
			exit()

	print(ans)
	return

if __name__ == "__main__":
	main()
