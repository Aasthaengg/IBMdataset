MOD = 10**9 + 7
S = input()
d = "ABC".index
s = [0]*4
s[0] = 1
for c in S:
    if c == "?":
        s = [s[0]*3, s[1]*3 + s[0], s[2]*3 + s[1], s[3]*3 + s[2]]
        for i in range(4):s[i] %= MOD
    else:
        i = d(c)
        s[i+1] += s[i] % MOD
print(s[3] % MOD)
