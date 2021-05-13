n = int(input())
a = [i for i in input()]
b = [i for i in input()]
c = [i for i in input()]
ans = 0

for j in range(len(a)):
	
	if a[j] == b[j] == c[j]:
		ans += 0
	elif a[j] != b[j] and b[j] != c[j] and a[j] != c[j]:
		ans += 2
	else:
		ans += 1

print(ans)
