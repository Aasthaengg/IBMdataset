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


def main():
	n=II()
	A=LI()
	A.sort()

	ans=1
	for i in A:
		ans*=i
		if ans>10**18:
			print(-1)
			exit()

	print(ans)








if __name__ == "__main__":
	main()
