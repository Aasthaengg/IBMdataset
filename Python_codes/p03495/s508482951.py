from collections import Counter

# input
N, K = map(int, input().split())
A = Counter(map(int, input().split()))

val = sorted(A.values())
print(sum(val[:len(val) - K]))