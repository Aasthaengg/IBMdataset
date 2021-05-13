import sys
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
# rstrip().decode()

def main():
	n=II()
	A=[0]+[II() for _ in range(n)]

	a=1

	for i in range(n+3):
		if a==2:
			ans=i
			break
		a=A[a]
	else:
		ans=-1

	print(ans)









if __name__ == "__main__":
	main()
