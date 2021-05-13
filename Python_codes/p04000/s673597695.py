def main():
	import sys
	input=sys.stdin.readline
	h,w,n=map(int,input().split())
	ans=[0]*10
	p=set()
	q=set()
	for i in range(n):
		a,b=map(int,input().split())
		for j in range(-1,2):
			for k in range(-1,2):
				if 2<=a+j<=h-1 and 2<=b+k<=w-1:
					r=(a+j)*(10**10)+b+k
					p.add(r)
		q.add(a*(10**10)+b)
	p=list(p)
	for x in p:
		cnt=0
		for j in range(-1,2):
			for k in range(-1,2):
				if x+j*(10**10)+k in q:
					cnt+=1
		ans[cnt]+=1
	print((h-2)*(w-2)-sum(ans[1:]))
	for i in range(1,10):
		print(ans[i])
if __name__ == '__main__':
	main()