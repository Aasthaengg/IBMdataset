N = int(input())
ans = 0
d = [1]*(1000010)
for k in range(2,1000010):
    t = 1
    while k*t <= 1000001:
        d[k*t] += 1
        t += 1
for M in range(1,N):
    ans += d[M]
print(ans)
