s = input()

l = 0
r = len(s)-1

ans = 0
flg = True
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    elif s[l] == 'x':
        l += 1
        ans += 1
    elif s[r] == 'x':
        r -= 1
        ans += 1
    else:
        flg = False
        break

if flg: print(ans)
else: print(-1)