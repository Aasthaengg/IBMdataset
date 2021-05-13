from collections import Counter
N = int(input())
A = [int(input()) for _ in range(N)]
c = Counter(A)
print(sum(tuple(map(lambda x: x % 2, c.values()))))