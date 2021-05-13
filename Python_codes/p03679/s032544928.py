import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines

# mod=10**9+7
# rstrip().decode('utf-8')
# map(int,input().split())
# import numpy as np

def main():
	x,a,b=map(int,input().split())
	
	ans="dangerous"
	
	if b-a<=0:
		ans="delicious"
	elif b-a<=x:
		ans="safe"
	
	print(ans)
	
	






	
if __name__ == "__main__":
	main()
