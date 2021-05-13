import bisect
a, b, q = map(int, input().split())
inf = 10**18
s = [-inf] + [int(input()) for _ in range(a)] + [inf]
t = [-inf] + [int(input()) for _ in range(b)] + [inf]
#print(s)
#print(t)
for _ in range(q):
    start = int(input())
    x = bisect.bisect_right(s, start)
    y = bisect.bisect_right(t, start)
    ans = inf
    for i in [s[x], s[x-1]]:
        for j in [t[y], t[y-1]]:
            res = min(abs(i-start) + abs(j-i), abs(j-start) + abs(i-j))
            ans = min(ans, res)
    print(ans)