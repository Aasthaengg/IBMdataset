S = input()
S = S.replace('BC','D')
ans = a = 0
for c in S:
    if c=='A':
        a += 1
    elif c=='D':
        ans += a
    else:
        a = 0
print(ans)