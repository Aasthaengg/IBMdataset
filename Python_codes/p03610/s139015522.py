S = input()
ans=[]
for i in range(len(S)):
	if i%2==0:
		ans.append(S[i])
ans=''.join(ans)
print(ans)