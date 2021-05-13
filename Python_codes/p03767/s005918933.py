N = int(input())
a = [int(i) for i in input().split()]
a.sort()
ans = 0
for i in range(1,N+1):
	#print(a[-2*i])
	ans += a[-2*i]

print(ans)

