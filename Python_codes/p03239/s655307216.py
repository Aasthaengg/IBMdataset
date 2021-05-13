n, t = map(int, input().split())
cts = [tuple(map(int, input().split())) for _ in range(n)]

c_ans = float('inf')
for ct in cts:
    if ct[1] <= t:
        c_ans = min(c_ans, ct[0])
if c_ans == float('inf'):
    print('TLE')
else:
    print(c_ans)
