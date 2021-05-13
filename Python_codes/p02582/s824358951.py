s = input()
ans = 0
for r in s:
    if r == 'R':
        ans += 1
if ans == 2 and s == 'RSR':
    print(1)
else:
    print(ans)