n = int(input())
m = 10**18
ans = 1
k = list(map(int, input().split()))
if 0 in k:
    ans = 0
else:
    for i in range(n):
        ans *= k[i]
        if (ans > m):
            ans = -1
            break
print(ans)
