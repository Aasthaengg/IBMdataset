from collections import Counter as C;r=range(3)
def s():
	H,W,N,*L=map(int,open(0).read().split());D={};M=[(H-2)*(W-2)]+[0]*9
	for a,b in zip(*[iter(L)]*2):
		for x in r:
			for y in r:
				if H-1>a-y>0<b-x<W-1:
					t=(a-y)*W+b-x
					D[t]=D.get(t,0)+1
	for k,v in C(D.values()).items():M[0]-=v;M[k]+=v
	print(*M)
if __name__=="__main__":s()