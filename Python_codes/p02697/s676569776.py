n,m = map(int, input().split())
a = (n-1) // 2
d = 1
memo = set([])
for i in range(m):
    if n-d in memo or 2*d == n:
        d += 1
    memo.add(d)
    print(a, a+d)
    a -= 1
    d += 2
