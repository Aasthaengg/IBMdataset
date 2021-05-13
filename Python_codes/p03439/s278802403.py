#%%
n = int(input())
s = [0] * (n + 1)

print(0)
a = input()
if a == 'Vacant':
    exit()
s[0], s[n] = a, a
l, r = 0, n
while True:
    m = (r + l) // 2
    print(m)
    a = input()
    if a == 'Vacant':
        exit()
    s[m] = a
    if s[l] == s[m]:
        if (l - m) % 2 == 1:
            r = m
        else:
            l = m
    else:
        if (l - m) % 2 == 1:
            l = m
        else:
            r = m
