n = int(input())
s = list(input())
mod = 10 ** 9 + 7
alph_count = [0] * 200
ans = 0
for i in s:
    m = ord(i)
    alph_count[m] += 1
    c = 1
    for j in range(97, 123):
        if not m == j:
            c *= alph_count[j] + 1
        c %= mod
    ans += c
    ans %= mod
print(ans)