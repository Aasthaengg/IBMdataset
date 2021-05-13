n=int(input())
s=[]
for _ in range(n):
	s.append(str(input()))

counter={}
ans=0
for i in range(n):
	ss = sorted(s[i])
	ss=("").join(ss)
	if ss not in counter:
		counter[ss]=0
	else:
		counter[ss]+=1
		ans+=counter[ss]

print(ans)