n = int(input())
h = list(map(int, input().split()))
ans = 0
ansb = 0
for i in range(n-1):
    if h[i + 1] <= h[i]:
        ansb += 1
        if ansb > ans:
            ans = ansb
    else:
        ansb = 0
print(ans)
