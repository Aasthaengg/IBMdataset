from math import sqrt

N, M = [int(_) for _ in input().split()]

p = []
m = M
max_x = 1
for i in range(2, int(sqrt(m)) + 1):
    if m % i == 0:
        cnt = 0
        while m % i == 0:
            cnt += 1
            m //= i
        p.append((i, cnt))
        if cnt > max_x:
            max_x = cnt
if m > 1:
    p.append((m, 1))

kaijo = [0] * (max_x + 1 + N)
gyaku = [0] * (max_x + 1 + N)
kaijo[0] = kaijo[1] = 1
gyaku[0] = gyaku[1] = 1

MOD = 10 ** 9 + 7
for i in range(2, len(kaijo)):
    kaijo[i] = (kaijo[i - 1] * i) % MOD
for i in range(2, len(gyaku)):
    gyaku[i] = pow(kaijo[i], MOD - 2, MOD)
# print(kaijo)
# print(gyaku)
ans = 1
for x, y in p:
    a = y + (N - 1)
    b = (N - 1)
    spam = (kaijo[a] * gyaku[a - b] * gyaku[b]) % MOD
    ans = (ans * spam) % MOD
print(ans)
