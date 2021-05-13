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

#2345
#import numpy as np

from itertools import combinations

def main():
	n=II()

	for i in range(10**3):
		if i*(i+1)==2*n:
			break
	else:
		print("No")
		exit(0)
	k=i+1

	ans=[[] for _ in range(k)]

	for i,a in enumerate(combinations(range(k),2)):
		ans[a[0]].append(i+1)
		ans[a[1]].append(i+1)
	#print(ans)

	print("Yes")
	print(k)
	for a in ans:
		print(k-1,*a)



if __name__ == "__main__":
	main()