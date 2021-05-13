n = int(input())
d, x = map(int, input().split())
A = []
for i in range(n):
	A.append(int(input()))
ans = n + x
d -= 1
for a in A:
	ans += d // a
print(ans)