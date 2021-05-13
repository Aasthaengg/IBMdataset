n = int(input())
h = list(map(int, input().split()))

ans = 0
tmp = 0

chain = False
ans = 0
tmp = 0
now = h[0]

for a in range(1, n):
    if now >= h[a]:
        if chain:
            tmp += 1
        else:
            tmp += 1
            chain = True
    else:
        chain = False
        tmp = 0
    ans = max(ans, tmp)
    now = h[a]

print(ans)
