import collections

n = int(input())
a = list(map(int, input().split()))
q = int(input())

d = collections.Counter(a)
ans = sum(a)

for i in range(q):
    b, c = map(int, input().split())
    num = (c-b)*d[b]
    ans += num
    print(ans)
    d[c] += d[b]
    d[b] = 0