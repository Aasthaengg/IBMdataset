n = int(input())
a = [int(i) for i in input().split()]

h = sum(a) / len(a)
ans = []

for i, j in enumerate(a):
	ans.append([abs(j - h), i])

print(sorted(ans)[0][1])