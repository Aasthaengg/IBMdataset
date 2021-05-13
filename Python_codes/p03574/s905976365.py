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
	h,w=MI()
	G=[[0]*(w+2)]
	for _ in range(h):
		G.append([0]+list(input())+[0])
	G.append([0]*(w+2))

	for i in range(h+2):
		for j in range(w+2):
			if G[i][j]==".":
				cnt=0
				for ii in range(i-1,i+2):
					for jj in range(j-1,j+2):
						if G[ii][jj]=="#":
							cnt+=1
				G[i][j]=cnt
	G=G[1:-1]

	for s in G:
		print(*s[1:-1],sep="")


if __name__ == "__main__":
	main()
