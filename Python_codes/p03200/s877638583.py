
s = input()
ans = 0
tmp = 0
#saving the number of black
for c in reversed(s):
    if c == 'W':
        tmp += 1
    else:
        ans += tmp
print(ans)