s = input()
L = 0
R = len(s)-1
ans = 0
while L < R:
    if s[L] == s[R]:
        L += 1
        R -= 1
    elif s[L] == 'x' and s[R] != 'x':
        ans += 1
        L += 1
    elif s[L] != 'x' and s[R] == 'x':
        ans += 1
        R -= 1
    elif s[L] != s[R] and s[L] != 'x' and s[R] != 'x':
        ans = -1
        break
print(ans)