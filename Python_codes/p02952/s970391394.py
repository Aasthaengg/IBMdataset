n = int(input())

def numlen(n):
	return len(str(n))

ans = 0
for j in range(1, n+1):
	if numlen(j)%2 == 1:
		ans += 1

print(ans)