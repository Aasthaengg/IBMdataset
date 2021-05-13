a=input()
p=len(a)
cnt=[0]*26
for i in range(p):
	cnt[ord(a[i])-ord("a")]+=1
ans=p*(p-1)//2+1
for x in cnt:
	ans-=x*(x-1)//2
print(ans)