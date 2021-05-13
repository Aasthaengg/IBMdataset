s = input()
n = len(s)
a = s[0:n//2]
b = s[n//2+1:n]
if s == s[::-1] and a == a[::-1] and b == b[::-1]:
    print('Yes')
else:
    print('No')