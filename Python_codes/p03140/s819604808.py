n = int(input())
a = input()
b = input()
c = input()

cnt = 0

for i in range(n):
	num_unique = len(list(set([a[i],b[i],c[i]])))

	if num_unique == 3:
		cnt += 2
	elif num_unique == 2:
		cnt += 1
	else:
		cnt += 0

print(cnt)