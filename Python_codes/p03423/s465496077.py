n = int(input())
ans = 0
if n > 2:
    for i in range(3, n + 1):
        k = n // i
        if ans < k:
            ans = k
print(ans)
