s=input()
w=int(input())
ans=''
for i in s[::w]:
	ans+=i
print(ans)
