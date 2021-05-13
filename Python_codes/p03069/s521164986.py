n = int(input())
s = input()

w = s.count('.')
b = n - w
ans = min(w, b)
r = 0
l = w
for si in s:
    if si == '#':
        r += 1
    else:
        l -= 1
    if ans > r + l:
        ans = r + l
print(ans)
