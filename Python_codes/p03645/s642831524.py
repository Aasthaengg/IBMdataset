n, m = map(int, input().split())
ans = [0]*(n+1)
for _ in [0]*m:
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if a==1:
        ans[b] += 1
    elif b==n:
        ans[a] += 1
if 2 in set(ans):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')