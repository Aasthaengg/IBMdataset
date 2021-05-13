import sys

t = []
for _ in range(3):
	a, b = map(int, input().split())
	t.append(a)
	t.append(b)

for i in [1,2,3,4]:
	if t.count(i) > 2:
		print("NO")
		sys.exit()

print("YES")