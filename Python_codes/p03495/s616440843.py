from collections import Counter
n, k = map(int, input().split())
A = Counter(list(map(int, input().split())))
B = sorted(A.items())
print(sum(sorted(A.values(), reverse=True)[k:]))