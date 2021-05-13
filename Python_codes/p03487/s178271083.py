import collections

N = int(input())
A = list(map(int, input().split()))

B = dict(collections.Counter(A))
M = len(B)

ans = 0

for i in B.keys():
    if B[i] >= int(i):
        ans += B[i] - int(i)
    else:
        ans += B[i]

print(ans)