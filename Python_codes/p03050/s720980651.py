def make_yakusu(n):
	yakusu=[]
	for i in range(1,int(n**0.5)+1):
		if n%i==0:
			yakusu.append(i)
			if i!=n//i:
				yakusu.append(n//i)
	return yakusu
x=int(input())
ans=0
yakusu=make_yakusu(x)
for i in yakusu:
	if x//i-1>=i+1:
		ans+=x//i-1
print(ans)
