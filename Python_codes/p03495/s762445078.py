from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
d = Counter(A).most_common()

if len(d) > K:
    print(sum(v for k, v in d[-(len(d) - K):]))
else:
    print(0)