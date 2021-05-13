n = int(input())
d = [int(i) for i in input().split()]
ret = 0
for i in range(n):
	for j in range(i + 1, n):
		ret += d[i] * d[j]
print (ret)