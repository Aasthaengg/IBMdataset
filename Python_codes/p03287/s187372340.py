import sys
from collections import defaultdict
bbn=1000000007
	
#+++++

		
def main():
	n, m = map(int, input().split())
	al = list(map(int, input().split()))
	bl= [0] * len(al)
	ruiseki=0
	ddi=defaultdict(lambda : 0)
	ddi[0]+=1
	for i,v in enumerate(al):
		ruiseki+=v
		bl[i] = ruiseki % m
		ddi[bl[i]] += 1
		
	ret=0
	for k in ddi:
		v=ddi[k]
		ret += v * (v - 1)//2
	
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