n, k = map(int, input().split())
list_A = list(map(int, input().split()))
a = list_A.index(1) + 1
ans = 0
cnt = 0
amari = 0
if a == 1:
    ans += 0
else:
    ans += (a-1)//(k-1)
    if (a-1)%(k-1) != 0:
        ans += 1
        cnt += 1
        amari += (a-1)%(k-1)

if a == n:
    ans += 0
else:
    ans += (n-a)//(k-1)
    if (n-a)%(k-1) != 0:
        ans += 1
        cnt += 1
        amari += (n-a)%(k-1)

if cnt == 2 and amari <= k-1:
    ans -= 1

print(ans)