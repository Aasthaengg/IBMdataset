import sys
#input = sys.stdin.readline
input = sys.stdin.buffer.readline

# mod=10**9+7
# rstrip().decode('utf-8')
# map(int,input().split())
# import numpy as np


def main():
	xy=list(map(int,input().split()))
	ans=0
	li=[0,3,2,1]

	for i in xy:
		if i<=3:
			ans+=li[i]

	if sum(xy)==2:
		ans+=4

	print(ans*100000)







if __name__ == "__main__":
	main()
