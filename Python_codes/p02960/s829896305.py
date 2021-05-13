from collections import defaultdict
s = input()[::-1]
mod = 13
p = 10 ** 9 + 7
dic = defaultdict(int)
dic[0] = 1

for i in range(len(s)):
    tmp = defaultdict(int)
    if s[i] == "?":
        for j in range(10):
            d = j * pow(10, i, mod)
            for k, v in dic.items():
                tmp[(k + d) % mod] += v
                tmp[(k + d) % mod] %= p
    else:
        d = int(s[i]) * pow(10, i, mod)
        for k, v in dic.items():
            tmp[(k + d) % mod] = v
    dic = tmp
print(dic[5] % p)
