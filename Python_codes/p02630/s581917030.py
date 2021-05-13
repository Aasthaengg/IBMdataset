n = int(input())
a = [int(x) for x in input().split()]
q = int(input())

count = [0] * (10**5 + 1)
S = [0] * (q + 1)
for i in range(n):
	count[a[i]] += 1
	S[0] += a[i]

for i in range(1, q + 1):
	b, c = [int(x) for x in input().split()]
	S[i] = S[i - 1]
	S[i] += (c - b) * count[b]
	count[c] += count[b]
	count[b] = 0
	
for i in range(1, q + 1):
	print(S[i])