n = int(input())
a = list(map(int, input().split()))

ruiseki = [0] * (n + 1)
ruiseki2 = [0] * (n + 1)
for i in range(n):
    ruiseki[i + 1] = ruiseki[i] + a[i]
    ruiseki2[i + 1] = ruiseki2[i] ^ a[i]

def solve(l, r):
    return ruiseki[r] - ruiseki[l] == ruiseki2[r] ^ ruiseki2[l]
  
ans = 0
for i in range(n):
    ok = i
    ng = n + 1
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if solve(i, mid):
            ok = mid
        else:
            ng = mid
    ans += ok - i
print(ans)