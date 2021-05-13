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
	n,k=MI()


	if k%2:
		a=n//k
		b=0
	else:
		a=n//k
		b=n//(k//2)-a

	print(a**3+b**3)








if __name__ == "__main__":
	main()
