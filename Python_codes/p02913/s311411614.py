n = int(input())
s = list(input())
b = 27
mod = 67280421310721
m = n // 2
x = [1] * (m + 1)
for i in range(1, m + 1):
    x[i] = (x[i - 1] * b) % mod
h0 = [0] * m
h0[0] = ord(s[0]) - 96
d = [{} for _ in range(m + 1)]
for i in range(1, m):
    h0[i] = (h0[i - 1] * b + (ord(s[i]) - 96)) % mod
for i in range(m, 0, -1):
    h = h0[i - 1]
    d[i][h] = 0
    for j in range(i, n):
        h *= b
        h %= mod
        h -= (x[i] * (ord(s[j - i]) - 96) % mod)
        h += (ord(s[j]) - 96)
        h %= mod
        if h in d[i]:
            if (j - i + 1 - d[i][h]) >= i:
                print(i)
                exit()
        else:
            d[i][h] = j - i + 1
print(0)