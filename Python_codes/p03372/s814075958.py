import sys

#+++++
	



def main():
	n, c = map(int, input().split())
	
	ll=[]
	for i in range(n):
		x,v=map(int, input().split())
		ll.append([x,v])
		
	ll.sort(key=lambda x:x[0])
	for i,v in enumerate(ll):
		ll[i].append(c - v[0])
	all_cal=sum([v[1] for v in ll])
	
	tw=0
	tc=0
	max_c=0
	max_cr=0
	for i,v in enumerate(ll):
		ptw=tw
		tw=v[0]
		tc+=v[1]
		
		#ll[i].append(v[1]-v[0]+ptw)
		cc=tc-tw
		max_c=max(cc,max_c)
		crc=tc-2*tw
		max_cr=max(crc, max_cr)
		#ll[i].append(cc)
		ll[i].append(max_c)
		#ll[i].append(crc)
		ll[i].append(max_cr)

	ll.sort(key=lambda x:-x[0])
	tw=0
	tc=0
	max_c=0
	max_cr=0
	for i,v in enumerate(ll):
		ptw=tw
		tw=v[2]
		tc+=v[1]
		
		#ll[i].append(v[1]-v[0]+ptw)
		cc=tc-tw
		max_c=max(cc,max_c)
		crc=tc-2*tw
		max_cr=max(crc, max_cr)
		#ll[i].append(cc)
		ll[i].append(max_c)
		#ll[i].append(crc)
		ll[i].append(max_cr)
		
	ll.sort(key=lambda x:x[0])
	ret_max=0
	for l in ll:
		#print(l)
		pass
	
	for l,lp in zip(ll,ll[1:]):
		r=l[3]+lp[6]
		ret_max=max(r,ret_max)
		
	for l,lp in zip(ll[-1::-1],ll[-2::-1]):
		r=l[5]+lp[4]
		ret_max=max(r,ret_max)
		
	ret_max=max(ret_max, ll[-1][3])
	ret_max=max(ret_max, ll[0][5])
				
	print(ret_max)
	
	
#+++++

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
	else:
		input = sys.stdin.readline
		
	ret = main()
	if ret is not None:
		print(ret)
		
	if sys.platform =='ios':
		sys.stdin.close()