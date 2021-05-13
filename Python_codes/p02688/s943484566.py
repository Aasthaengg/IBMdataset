import collections
N,K = map(int, input().split())
d = [0] * K
A = [0] * K
for i in range(K):
    d[i] = int(input())
    A[i] = list(map(int, input().split()))
B = []
for l in range(K):
    B += A[l]
c = collections.Counter(B)
values, counts = zip(*c.most_common())
ans = N - len(values)
print(ans)