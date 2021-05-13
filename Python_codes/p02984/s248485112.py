import sys
#import numpy as np

#+++++
		
def main2():
	n = int(input())
	water_list=list(map(int, input().split()))
	
	mw=water_list[-1]
	for i in range(mw+1):
		cv = mw - i
		init_cv=cv
		for w in water_list[::-1]:
			#print(w,cv, w-cv)
			cv = w - cv
			if cv < 0:
				break
		else:
			#print('hhh', cv, init_cv, mw)
			if init_cv == cv:
				ret = [0 for _ in range(n)]
				cv=init_cv
				for ii, ww in enumerate(water_list):
					ret[ii] = cv*2
					cv = ww - cv
					#print(ret)
				return ret
				
	return 'hoge'
	
def main():
	n = int(input())
	water_list=list(map(int, input().split()))
	a = sum(water_list) - 2*sum(water_list[1::2])
	ret = [a]
	next=a
	for v in water_list[:-1]:
		next = (v*2 - next)
		ret.append(next)
	
	print(*ret)
	
#+++++

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		
	ret = main()
	if ret is not None:
		print(' '.join([str(i) for i in ret]))