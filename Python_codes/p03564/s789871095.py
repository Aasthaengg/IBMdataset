n=int(input())
k=int(input())
ans=1
for i in range(n):
	ans+=(ans if ans*2<ans+k else k)

print(ans)
