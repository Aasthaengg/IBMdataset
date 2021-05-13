s = list(input())
n = len(s)
s.append('<')
mini = 0
maxi = 0
p = 0

for i in range(n):
    if s[i] == '<':
        mini += 1
    else:
        maxi += 1
        if s[i+1] == '<':
            m = max(mini,maxi)
            p += (1 + m) * m // 2
            m = min(mini,maxi) - 1
            p += (1 + m) * m // 2
            mini = 0
            maxi = 0

if mini != 0:
    print(p + ((1+mini) * mini // 2))
else:
    print(p)