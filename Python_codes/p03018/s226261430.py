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
	s=RD()[::-1]+"DDDDD"

	i=0
	cnt=0
	ans=0

	#print(s)

	while i<=len(s)-3:
		if s[i:i+2]=="CB":
			cnt+=1
			i+=2
		elif s[i]=="A":
			ans+=cnt
			i+=1
		else:
			cnt=0
			i+=1
	print(ans)





if __name__ == "__main__":
	main()
