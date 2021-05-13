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

from collections import defaultdict

def main():
	h,w=MI()
	d=defaultdict(int)

	for _ in range(h):
		s=RD()
		for i in s:
			d[i]+=1

	dd=defaultdict(int)

	for k,v in d.items():
		q,r=divmod(v,4)
		dd[4]+=q
		qq,rr=divmod(r,2)
		dd[2]+=qq
		dd[1]+=rr
	#print(dd)


	ans="Yes"

	if h%2==0 and w%2==0:
		if dd[2]!=0 or dd[1]!=0:
			ans="No"

	elif h%2==0:
		if dd[1]!=0 or dd[2]>h//2:
			ans="No"

	elif w%2==0:
		if dd[1]!=0 or dd[2]>w//2:
			ans="No"

	else:
		if dd[1]!=1:
			ans="No"
		else:
			if dd[2]>h//2+w//2:
				ans="No"

	print(ans)


















if __name__ == "__main__":
	main()
