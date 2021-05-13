n=int(input())
ans=0
for i in range(n):
	s1,s2=map(int,input().split())
	ans+=s2-s1+1
print(ans)