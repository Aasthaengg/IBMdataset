from collections import Counter

N = int(input())
A = [int(x) for x in input().split()]

c = Counter(A)

for i in range(N):
    print(c[i + 1])
