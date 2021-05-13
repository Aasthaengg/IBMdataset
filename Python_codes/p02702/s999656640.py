s = input()

d = [0 for i in range(len(s) + 1)]
i = len(s) - 1
deg = 1
while i >= 0:
    d[i] = (int(s[i]) * deg + d[i + 1]) % 2019
    deg = (deg * 10) % 2019
    i -= 1

#print(d)

cnt = [0 for i in range(2019)]
for i in d:
    cnt[i] += 1

res = 0
for i in cnt:
    res += i * (i - 1) // 2

print(res)
