N, M = map(int, input().split())

mn = 0
mx = 10**6

for i in range(M):
    l, r = map(int, input().split())
    mn = max(l, mn)
    mx = min(r, mx)

result = max(0, mx - mn + 1)
print(result)
