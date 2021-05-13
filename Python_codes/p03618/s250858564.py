from collections import Counter

A = input()
N = len(A)

c = Counter(A)
ans = 1 + N*(N-1)//2 - sum((v*(v-1))//2 for v in c.values())

print(ans)
