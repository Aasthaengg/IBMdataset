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
# rstrip().decode()

#import numpy as np

def main():
	s=input()
	n=len(s)
	ans="Yes"

	if s!=s[::-1] or s[:(n-1)//2]!=s[:(n-1)//2][::-1] or s[(n+3)//2-1:]!=s[(n+3)//2-1:][::-1]:
		ans="No"

	print(ans)

if __name__ == "__main__":
	main()
