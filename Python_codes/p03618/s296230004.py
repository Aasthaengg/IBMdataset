cnt={}
tot=0

ans=1

for i,c in enumerate(input(),0):
	if c in cnt:
		ans+=i-cnt[c]
	else:
		cnt[c]=0
		ans+=i
	cnt[c]+=1

print(ans)
