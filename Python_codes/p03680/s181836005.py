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
	A=[II() for _ in range(n)]

	#print(A)

	now=0
	cnt=1
	ans=-1
	for i in range(n+5):
		now=A[now]-1
		if now==1:
			ans=cnt
			break
		elif now==0:
			break
		else:
			cnt+=1
	print(ans)




if __name__ == "__main__":
	main()
