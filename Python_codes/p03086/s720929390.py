b=list(str(input()))
E={"A","C","G","T"}
count=0
ans=0
for moji in b:
	if moji in E:
		count+=1
	else:
		ans=max(ans,count)
		count=0
ans=max(ans,count)
print(ans)