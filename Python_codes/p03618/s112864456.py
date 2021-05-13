cnt=[0]*200

ans=1

for i,c in enumerate(input()):
	ans+=i-cnt[ord(c)]
	cnt[ord(c)]+=1

print(ans)
