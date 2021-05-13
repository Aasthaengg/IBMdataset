s = input()
t = s[::-1]
n = len(s)
a = s[:(n - 1) // 2]
b = t[:(n - 1) // 2]

if s == t and a == a[::-1] and b == b[::-1]:
    print('Yes')
else:
    print('No')