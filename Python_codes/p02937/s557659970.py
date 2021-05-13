import sys
#input = sys.stdin.readline
input = sys.stdin.buffer.readline

# mod=10**9+7
# rstrip().decode('utf-8')
# map(int,input().split())
# import numpy as np

from collections import defaultdict
import bisect

def main():
	s=input().rstrip().decode('utf-8')
	t=input().rstrip().decode('utf-8')

	D=defaultdict(list)

	for i in range(len(s)):
		D[s[i]].append(i+1)

	now=0
	cnt=0

	for i in t:
		if D[i]==[]:
			print(-1)
			exit(0)
		else:
			idx=bisect.bisect_right(D[i],now)
			try:
				now=D[i][idx]
			except:
				now=D[i][0]
				cnt+=1
	print(cnt*len(s)+now)
















if __name__ == "__main__":
	main()
