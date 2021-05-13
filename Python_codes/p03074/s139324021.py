n,k=map(int,input().split())
s=input()
cnt=[]
now=s[0]
p=0
for i in range(n):
	if s[i]==now:
		p+=1
	else:
		cnt.append(p)
		now=s[i]
		p=1
cnt.append(p)
ans=0
r=[]
cum_sum=0
for i in range(len(cnt)):
	cum_sum+=cnt[i]
	r.append((cnt[i],cum_sum))
for i in range(len(r)):
	if s[r[i][1]-r[i][0]]=="1":
		e=r[min(i+2*k,len(r)-1)][1]-r[i][1]+r[i][0]
	else:
		e=r[min(i+2*k-1,len(r)-1)][1]-r[i][1]+r[i][0]
	ans=max(ans,e)
print(ans)