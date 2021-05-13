a1, a2 = map(int, input().split())
a3, a4 = map(int, input().split())
a5, a6 = map(int, input().split())

ans = []

ans.append(a1)
ans.append(a2)
ans.append(a3)
ans.append(a4)
ans.append(a5)
ans.append(a6)

max = 0

for i in ans:
	if max < ans.count(i):
		max = ans.count(i)

print("YES" if max <= 2 else "NO")