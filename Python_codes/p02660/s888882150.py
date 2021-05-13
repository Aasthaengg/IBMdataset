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

	while n%2==0:
		d[2]+=1
		n//=2

	f=3
	while f*f<=n:
		if n%f==0:
			d[f]+=1
			n//=f
		else:
			f+=2

	if n!=1:
		d[n]+=1

	#print(d)

	ans=0

	for _,v in d.items():
		for i in range(1,10000):
			if (i*(i+1))//2>v:
				ans+=i-1
				break
	print(ans)
















if __name__ == "__main__":
	main()
