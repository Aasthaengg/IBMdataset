N = int(input())
A = list(map(int, input().split()))
A.sort()
old = A[0]
a = 1
ans = 0
for i in range(1, N):
    cur = A[i]
    if cur == old:
        a += 1
    else:
        if old <= a:
            ans += a - old
        else:
            ans += a
        a = 1
    old = cur
if old <= a:
    ans += a - old
else:
    ans += a
print(ans)