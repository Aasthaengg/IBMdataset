n, m = map(int, input().split())
MOD = 10**9+7

if m >= n//2+1:
    print(0)
    exit()

a = [True]*(n+1)
for i in range(m):
    a[int(input())] = False

p = [0]*(n+1)
for i in range(1, n+1):
    if i == 1:
        if a[i]:
            p[i] += 1
        continue
    if i == 2:
        if a[i]:
            p[i] += 1

    if a[i]:
        p[i] += p[i-1] + p[i-2]
        p[i] %= MOD
print(p[n])