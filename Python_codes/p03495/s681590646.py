from collections import Counter
N,K = map(int, input().split())
A = Counter(list(map(int, input().split())))
B = A.values()
k = len(B) - K
if k <= 0:
    print(0)
else:
    print(sum(sorted(B)[0:k]))