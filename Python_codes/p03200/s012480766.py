s = input()
b = 0
ans = 0
for i in s:
    if i=='B':
        b += 1
    else:
        ans += b
print(ans)