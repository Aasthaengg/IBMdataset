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

	a=0
	b=0
	ab=0
	ans=0

	for _ in range(n):
		s=input().rstrip().decode()
		ans+=s.count("AB")
		if s[0]=="B" and s[-1]=="A":
			ab+=1
		elif s[0]=="B":
			b+=1
		elif s[-1]=="A":
			a+=1

	if ab==0:
		ans+=min(a,b)
	else:
		ans+=ab-1
		if not a==b==0:
			ans+=1+min(a,b)

	print(ans)







if __name__ == "__main__":
	main()
