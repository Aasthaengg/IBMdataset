import bisect

S = list(str(input()))
T = list(str(input()))

X = [[] for _ in range(26)]
for i, c in enumerate(S):
    # a = 0, b = 1, ..., z = 25
    j = ord(c) - ord('a')
    X[j].append(i + 1)

q = 0
r = 0

for c in T:
    # a = 0, b = 1, ..., z = 25
    j = ord(c) - ord('a')

    if len(X[j]) == 0:
        print(-1)
        exit()

    idx = bisect.bisect_right(X[j], r)

    if idx == len(X[j]):
        q += 1
        r = X[j][0]
    else:
        r = X[j][idx]

ans = q * len(S) + r
print(ans)
