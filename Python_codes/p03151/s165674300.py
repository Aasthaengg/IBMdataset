n = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]

ans = 0

if sum(a) >= sum(b):
    diff = [a[i]-b[i] for i in range(n)]
    diff.sort()
    shortage = 0
    for i in diff:
        if i < 0:
            ans += 1
            shortage += (-i)
        else:
            break
    idx = n-1
    while shortage > 0:
        shortage -= diff[idx]
        idx -= 1
        ans += 1
else:
    ans = -1
print(ans)