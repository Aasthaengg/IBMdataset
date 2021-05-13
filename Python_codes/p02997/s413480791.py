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

	kk=(n-1)*(n-2)//2-k

	if kk<0:
		print(-1)
		exit()

	ans=[]
	#print(kk)
	for i in range(1,n):
		ans.append([i,n])
	#print(ans)

	for i in range(1,n):
		for j in range(i+1,n):
			if kk>0:
				kk-=1
				ans.append([i,j])

	print(len(ans))
	for i,j in ans:
		print(i,j)













if __name__ == "__main__":
	main()
