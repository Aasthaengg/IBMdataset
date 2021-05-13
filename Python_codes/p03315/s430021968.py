s = input()
ans = 0
for si in s:
    ans += (si == "+")
    ans -= (si == "-")
print(ans)
