N = int(input())

m = 1
ans = 0
while m*m <= N:
    if (N-m)%m == 0:
        d = (N-m)//m
        if d <= m: break
        ans += d
    m += 1
print(ans)