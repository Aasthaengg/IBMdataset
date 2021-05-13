s = input()

ans = 0
num = 0
for c in s:
    if c == 'T':
        num -= 1
    else:
        num += 1
    if num < 0:
        ans += 1
        num = 0

ans += num
print(ans)
