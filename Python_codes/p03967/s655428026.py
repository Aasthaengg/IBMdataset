s = input()

sg = 0
sp = 0
ans = 0

for i in range(len(s)):
    if sp+1 <= sg and s[i] == 'g':
        sp += 1
        ans += 1
    elif sp+1 > sg and s[i] == 'p':
        sg += 1
        ans -= 1
    elif sp+1 <= sg and s[i] == 'p':
        sp += 1
    else:
        sg += 1
print(ans)
