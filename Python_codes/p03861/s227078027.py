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
	a,b,x=MI()
	ans=(b-a)//x

	c=a+x*ans

	if b//x*x==-(-c//x)*x:
		ans+=1

	print(ans)






if __name__ == "__main__":
	main()
