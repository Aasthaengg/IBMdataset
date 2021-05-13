from collections import Counter
N, K = map(int, input().split())
A = Counter(list(map(int, input().split()))).most_common()
B = sorted([a[1] for a in A])
print(sum(B[:max(0, len(B)-K)]))