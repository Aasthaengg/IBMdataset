n, k = map(int, input().split())

def choose(n, m):   #0~nからm個選ぶ和の種類
    return (n - m + 1) * m + 1

s = 0
for i in range(k, n + 2):
    s += choose(n, i)

s %= (10**9 + 7)
print(s)
