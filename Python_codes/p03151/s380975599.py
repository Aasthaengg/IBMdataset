import sys
if sys.platform=='ios':
	sys.stdin=open('input_file.txt')
	
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans=0
if sum(A)<sum(B):
	ans=-1
	
else:
	cnt=0
	res=[]
	for i in range(N):
		if A[i]>=B[i]:
			res.append(A[i]-B[i])
		else:
			cnt+=B[i]-A[i]
			ans+=1
	if cnt>0:
		ans+=1
		res=sorted(res)[::-1]
		for i in range(len(res)):
			if res[i]<cnt:
				ans+=1
				cnt-=res[i]
			else:
				break

print(ans)