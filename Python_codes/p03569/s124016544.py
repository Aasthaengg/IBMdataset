from collections import Counter

s = input()
snotx = "".join([ch for ch in s if ch != 'x'])

if s == s[::-1]:
    print(0)
    exit()

if snotx != snotx[::-1]:
    print(-1)
    exit()

# 回数を合わせる
# print(s)
# print(snotx)

# xのrun-length
rl = []
i = 0
while i < len(s): 
    j = i
    while j < len(s) and s[j] == 'x':
        j += 1
    rl.append(j - i)
    i = j + 1
if s[-1] != 'x':
    rl.append(0)

# run-lengthの左右を見て合わせる
res = 0
i = 0
while i * 2 < len(rl):
    res += max(rl[i], rl[len(rl) - i - 1]) - min(rl[i], rl[len(rl) - i - 1])
    i += 1
print(res)
