s = str(input())
l = len(s)
b = s.count('B')
ans = 0
for i in range(l):
    if s[i] == 'B':
        ans += l - b - i
        b -= 1
print(ans)
