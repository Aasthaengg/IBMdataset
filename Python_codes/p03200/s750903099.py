s = list(input())
n = len(s)
m = s.count('B')
p = 0
for i in range(n-1):
    if s[i] == 'B':
        p += (n-m) - (i)
        m -= 1

print(p)