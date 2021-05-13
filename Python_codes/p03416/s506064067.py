a, b = map(int, input().split())
cnt=0
for i in range(a, b + 1):
	l = [int(c) for c in list(str(i))]
	l2 = l[::-1]
	if l2 == l:
		cnt += 1
print(cnt) 