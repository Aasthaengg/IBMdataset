n = int(input())
A = tuple(map(int, input().split()))

from collections import Counter
CA = Counter(A)
cu2 = 0
for k, v in CA.items():
    cu2 += v-1

print(len(A) - cu2 - cu2%2)
