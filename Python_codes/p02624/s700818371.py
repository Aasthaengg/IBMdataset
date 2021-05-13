N = int(input())

f = [0] * (N+1)

for i in range(1, N+1):
    cnt = i
    while cnt <= N:
        f[cnt] += 1
        cnt += i

ans = 0

for i in range(1, N+1):
    ans += i*f[i]

print(ans)