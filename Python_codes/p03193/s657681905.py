n, h, w = map(int, input().split())
a,b = [],[]
for _ in range(n):
	ta, tb = map(int, input().split())
	a.append(ta)
	b.append(tb)
cnt = 0
for i in range(n):
	if a[i] >= h and b[i] >= w:
		cnt += 1

print(cnt)