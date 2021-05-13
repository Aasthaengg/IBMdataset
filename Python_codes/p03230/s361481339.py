n = int(input())
l = []
i = 1
while n > 0:
	n -= i
	t = i * (i - 1) // 2
	l += [list(range(t + 1, t + i + 1))]
	i += 1
if n < 0:
	print("No")
	exit()
print("Yes")
ans = []
i -= 1
for j in range(i):
	ans.append(list(map(str, [i] + l[j] + [l[k][j] for k in range(j + 1, i)])))
ans.append(list(map(str, [i] + [l[j][-1] for j in range(i)])))
print(i + 1)
print(*map(" ".join, ans))