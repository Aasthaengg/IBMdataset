s=list(str(input()))
ans=[]
for i in s:
	if i not in ans:
		ans.append(i)

if len(ans)==2:
	print("Yes")
else:
	print("No")