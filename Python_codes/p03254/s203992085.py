n, x = [int(i) for i in input().split()]
A = sorted([int(i) for i in input().split()])

ans = 0
for i in range(n):
    if A[i] <= x:
        if i == n - 1:
            if x == A[i]:
                ans += 1
        else:
            x -= A[i]
            ans += 1
    else:
        break
print(ans)
