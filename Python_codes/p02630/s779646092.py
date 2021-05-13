import collections
N = int(input())
A = list(map(int, input().split()))
cnt = collections.Counter(A)
Q = int(input())
ans = []
s = sum(A)
for _ in range(Q):
    b, c = map(int, input().split())
    n = cnt[b]
    if b in cnt:
        cnt[c] += cnt[b]
        del cnt[b]
    s += (c-b)*n
    print(s)