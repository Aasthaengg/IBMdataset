n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a = sorted(a)
b = sorted(b)
c = sorted(c)

ans = 0

for i in range(n):
    ans1 = 0
    ans2 = 0
    ok = -1
    ng = n
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if a[mid] < b[i] :
            ok = mid
        else:
            ng = mid
        if abs(ng - ok) == 1:
            ans1 += ok + 1
    ok = n
    ng = -1
    while abs(ng - ok) > 1:
        mid = (ok + ng) // 2
        if b[i] < c[mid]:
            ok = mid
        else:
            ng = mid
        if abs(ng - ok) == 1:
            ans2 += n - ok
    ans += ans1 * ans2
print(ans)