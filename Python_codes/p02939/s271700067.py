s = input()
a = 0
b = 1
c = 1
d = 2
n = len(s)
ans = 0
while(True):
    if s[a:b] == s[c:d]:
        d += 1
    else:
        a = c
        b = d
        c = b
        d = c + 1
        ans += 1
    if d == n+1:
        break
print(ans+1)
