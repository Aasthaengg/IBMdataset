n, m = map(int, input().split())
div = m//n
INF = 10**18
ans = -INF
for i in reversed(range(1, div+1)):
    if m % i != 0:
        continue
    if ans < i:
        ans = i
        break
print(ans)
