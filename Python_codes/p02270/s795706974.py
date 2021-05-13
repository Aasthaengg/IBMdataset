n, k = map(int,input().split())
ws = []
for _ in range(n):
    t = int(input())
    ws.append(t)

def check(m):
    need = 1
    sm = 0
    for w in ws:
        if w > m:
            return False
        if sm + w > m:
            need += 1
            sm = w
        else:
            sm += w
    return need <= k

lw = 0
hi = 10**10
ans = hi
while lw <= hi:
    mid = (lw + hi) // 2
    if check(mid):
        ans = mid
        hi = mid - 1
    else:
        lw = mid + 1

print(ans)


