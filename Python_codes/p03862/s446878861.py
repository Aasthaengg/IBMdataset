n, x = list(map(int, input().split()))
al = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i == 0:
        if al[i] > x:
            ans += al[i]-x
            al[i] = x
    else:
        if al[i] + al[i-1] > x:
            ans += al[i] + al[i-1] - x
            al[i] = x - al[i-1]
print(ans)
