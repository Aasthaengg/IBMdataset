from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))
count_A = Counter(A)
sortA = [c for ai, c in count_A.most_common()]
print(sum(sortA[K:]))