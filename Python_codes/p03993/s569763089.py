a = int(input())
l = list(map(int,input().split()))
ans = 0
for e , i in enumerate(l):
	if (e+1) == l[i-1]:
		ans +=1
print(ans//2)