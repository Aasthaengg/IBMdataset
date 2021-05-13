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
	A=LI()
	A.sort()
	ans=0

	if A[0]%2 and A[1]%2 and A[2]%2:
		ans=A[0]*A[1]

	print(ans)




if __name__ == "__main__":
	main()
