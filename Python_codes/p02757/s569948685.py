n, p = map(int, input().split())
s = list(map(int, list(input())))

if p in [2, 5]:
    ans = 0
    for i, x in enumerate(s):
        if x % p == 0:
            ans += i + 1
    print(ans)
    exit()

x = [0] * p
x[0] = 1
temp = 0
d = 1
for i in range(n-1, -1, -1):
    temp = (temp + s[i] * d) % p
    x[temp] += 1
    d = (d * 10) % p

ans = 0

for z in x:
    ans += z * (z-1) // 2

print(ans)
