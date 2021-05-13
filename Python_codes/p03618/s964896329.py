import sys
from collections import defaultdict

bbn=1000000007
	
#+++++
#Reverse and Compare
#https://atcoder.jp/contests/agc019/tasks/agc019_b


def main():
	s = input()
	di = defaultdict(lambda : 0)
	for c in s:
		di[c] += 1
	
	total_s=len(s)
	ret=1
	
	for c in s:
		ret += total_s-1
		ret -= di[c]-1
		total_s -= 1
		di[c] -= 1
		
	print(ret)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)