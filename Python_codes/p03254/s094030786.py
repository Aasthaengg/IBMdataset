n, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i, a in enumerate(A):
    if i != n-1:
        if x >= a:
            ans += 1
            x -= a
        else:
            break
    else:
        if x == a:
            ans += 1
        else:
            break
print(ans)
