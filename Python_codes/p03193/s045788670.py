n,h,w = (int(i) for i in input().split())
ans = 0
for _ in range(n):
	a,b = (int(i) for i in input().split())
	if h<=a and w<=b: ans+=1
print(ans)