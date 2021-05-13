import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return float(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

from collections import deque

def main():
	mod=10**9+7
	n,k=MI()
	G=[[] for _ in range(n+1)]

	for _ in range(n-1):
		a,b=MI()
		G[a].append(b)
		G[b].append(a)
	#print(G)

	ans=k

	for i in range(len(G[1])):
		ans*=k-i-1
		ans%=mod
	#print(ans)

	Q=deque(G[1])
	#print(Q)

	sumi=set([1]+G[1])
	#print(sumi)


	while Q:
		now=Q.popleft()
		kk=k-2
		for i in G[now]:
			if i not in sumi:
				ans*=kk
				ans%=mod
				kk-=1
				sumi.add(i)
				Q.append(i)

	print(ans%mod)


























if __name__ == "__main__":
	main()
