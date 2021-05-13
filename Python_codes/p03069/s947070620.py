n = int(input())
s = input()
ans = 0
w = s.count('.')
b = 0
ans = w+b
for c in s:
    if c=='#':
        b += 1
    else:
        w -= 1
    ans = min(ans, w+b)
print(ans)
