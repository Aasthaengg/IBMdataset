import sys
read = sys.stdin.buffer.read
#input = sys.stdin.readline
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
# rstrip().decode('utf-8')


def main():
	n=II()
	
	ans=0
	for i in range(1,n+1):
		if i%3!=0 and i%5!=0:
			ans+=i
	
	print(ans)
	
if __name__ == "__main__":
	main()
