n = int(input())
a_list = list(map(int, input().split()))
counts = {}
for a in a_list:
	if a in counts:
		counts[a] += 1
	else:
		counts[a] = 1
counts = sorted(counts.items(), reverse=True, key=lambda x: x[0])
a = 0
b = 0
for key, value in counts:
	if value > 1:
		if a == 0:
			a = key
			if value > 3:
				b = key
				break
		else:
			b = key
			break
r = a*b
print(r)