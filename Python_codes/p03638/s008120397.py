import sys
bbn=1000000007
	
#+++++
		
def main():
	h, w = map(int, input().split())
	n = int(input())
	al = list(map(int, input().split()))
	
	al_i=0
	rr=[]
	for hi in range(h):
		ww=[-1]*w
		for wj in range(w):
			ww[wj] = al_i+1
			al[al_i] -= 1
			if al[al_i]==0:
				al_i+=1
		rr.append(ww)
		
	for i, r in enumerate(rr):
		b = r[:] if i % 2 == 0 else r[::-1]
		print(' '.join([str(v) for v in b]))
		
	
	
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