import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines

# rstrip().decode('utf-8')
# map(int,input().split())
# import numpy as np

inf=10**18

import bisect

def main():
	a,b,q=map(int,input().split())
	s=[-inf]+[int(input()) for _ in range(a)]+[inf]
	t=[-inf]+[int(input()) for _ in range(b)]+[inf]
	x=[int(input()) for _ in range(q)]
	
	
	for i in x:
		si=bisect.bisect_left(s,i)
		ti=bisect.bisect_left(t,i)
		
		ans=inf
		for S in [s[si-1],s[si]]:
			for T in [t[ti-1],t[ti]]:
				ans=min(ans,abs(S-i)+abs(S-T),abs(T-i)+abs(S-T))
		print(ans)
		
		
		
	

if __name__ == "__main__":
	main()
