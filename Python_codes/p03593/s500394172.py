from collections import Counter
C = Counter()
h, w = map(int, input().split())
for _ in range(h):
	C += Counter(input())
lim = (h // 2) * (w % 2) + (w // 2) * (h % 2)
cnt = flg = 0
for k, v in C.items():
	while v >= 4:
		v -= 4
	if v >= 2:
		cnt += 1
		if cnt > lim:
			print("No")
			exit()
	if v % 2:
		if flg or h % 2 == w % 2 == 0:
			print("No")
			exit()
		flg = 1
print("Yes")