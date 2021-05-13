N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
max_profit = a[1] - a[0]
min_val = min(a[1],a[0])
for i in range(2,N):
	if a[i] < min_val:
		min_val = a[i]
	elif a[i] - min_val > max_profit:
		max_profit = a[i] - min_val
print(str(max_profit))