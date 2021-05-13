s = input()

i = 1
ans = ''
for x in s:
    if i & 1:
        ans += x
    i += 1
print(ans)