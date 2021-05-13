import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines

# mod=10**9+7
# rstrip().decode('utf-8')
# map(int,input().split())
# import numpy as np

def main():
	n=int(input())
	A=list(map(int,input().split()))
	
	ans="YES"
	
	if sum(A)%2:
		ans="NO"
	
	print(ans)
	
if __name__ == "__main__":
	main()
