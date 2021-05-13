from collections import Counter

s = input()
snotx = "".join([ch for ch in s if ch != 'x'])

if s == s[::-1]:
    print(0)
    exit()

if snotx != snotx[::-1]:
    print(-1)
    exit()

# 両端から見てくる (解説解法)
index_l = 0
index_r = len(s) - 1
count = 0
while index_l < index_r:
    if s[index_l] == s[index_r]:
        index_l += 1
        index_r -= 1
    elif s[index_l] == 'x':
        count += 1
        index_l += 1
    elif s[index_r] == 'x':
        count += 1
        index_r -= 1
    else:
        print(-1)
        exit()
print(count)