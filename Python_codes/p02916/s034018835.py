n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=0
j=0
for i in a:
	ans+=b[i-1]
	if i==j+1 and i!=1:
		ans+=c[j-1]
	j=i
print(ans)