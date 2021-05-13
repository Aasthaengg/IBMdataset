input()
a = [0] + list(map(int, input().split()))
cnt = 0
for i, target in enumerate(a):
	if i == a[target]:
		cnt += 1
print(cnt // 2)
