s = input()
ans = 0
for ss in s:
    if ss == '-':
        ans -= 1
    else:
        ans += 1
print(ans)
