from collections import defaultdict

f = defaultdict(list)
d = {}


s = list(input())
t = list(input())

len_s = len(s)

for i in range(len_s):
    f[s[i]].append(i)

next_char = [[0] * len_s for _ in range(len(f))]

j = 0
for k, v in f.items():
    d[k] = j
    l = 0
    for i in range(len_s):
        if v[l] == i:
            l += 1
            if l == len(v):
                l = 0
        next_char[j][i] = v[l]
    j += 1

m = 0

for i in range(len(t)):
    x = t[i]
    if i == 0 and t[i] == s[i]:
        continue 
    if d.get(x) == None:
        m = -2
        break
    else:
        j = d[x]
        r = m % len_s
        n = next_char[j][r]
        if r >= n:
            m += len_s - (r-n)
        else:
            m += n - r

print(m+1)

