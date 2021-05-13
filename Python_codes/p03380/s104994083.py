n = int(input())
a = list(map(int,input().split()))
a.sort()
min = a[-1]
j = 0
for i in range(n-1):
	if abs(a[i] - a[-1]//2) <= min:
		min = abs(a[i] - a[-1]//2)
		j = i
L = [a[-1],a[j]]
print(*L)