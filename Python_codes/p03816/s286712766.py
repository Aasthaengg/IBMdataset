import collections
N = int(input())
A = list(map(int, input().split()))

C = collections.Counter(A)

ctr = 0
for c in C.items():
	ctr += c[1] - 1

eat_card = 2 * ((ctr + 1) // 2)	
print(N - eat_card)