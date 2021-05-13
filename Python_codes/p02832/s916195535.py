n = int(input())
aa = [int(i) for i in input().split()]
idx = 1
for a in aa:
	if a == idx:
		idx += 1
if idx == 1:
	ret = -1
else:
	ret = n - idx + 1
print(ret)