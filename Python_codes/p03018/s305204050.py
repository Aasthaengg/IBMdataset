s=input()
cnt=ans=0
i=0
while i<len(s)-1:
	if s[i]=="A":
		cnt+=1
		i+=1
	elif s[i]+s[i+1]=="BC":
		ans+=cnt
		i+=2
	else:
		cnt=0
		i+=1
print(ans)