n = int(input())
p = list(map(int,input().split()))
ans = 0
i = 0

p.append(0)

while i <= n-1:
	if p[i] == i+1 and p[i+1] == i+2:
		i += 2
		ans += 1
	elif p[i] == i+1 and p[i+1] != i+2:
		i += 1
		ans += 1
	else:
		i += 1

print(ans)