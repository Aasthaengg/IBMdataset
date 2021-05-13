n, k = map(int, input().split())
a = list(map(int, input().split()))
r = 0
s = {0: [0]}
for i in range(n):
    r = (r + a[i] - 1) % k
    if r in s:
        s[r].append(i + 1)
    else:
        s[r] = [i + 1]
ret = 0
for key in s:
    a = s[key]
    en = 0
    for st in range(len(a)):
        while en < len(a) and a[en] - a[st] < k:
            en += 1
        ret += en - st - 1
print(ret)