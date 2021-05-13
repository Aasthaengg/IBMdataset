import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines


# mod=10**9+7
# rstrip().decode('utf-8')
# map(int,input().split())
#import numpy as np

def main():
	n,m=map(int,input().split())
	s=input().rstrip().decode('utf-8')
	t=s[::-1]
	
	ans=[]
	
	now=0
	while now<n:
		for i in range(min(m,n-now),0,-1):
			
			if t[now+i]=="0":
				now+=i
				ans.append(i)
				break
			else:
				continue
		else:
			print(-1)
			exit(0)
	
	print(*ans[::-1])
	
	
	
	
	
	
	



if __name__ == "__main__":
	main()
