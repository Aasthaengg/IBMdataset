s = input()+chr(ord("a")-1)
ans = -1
for i in range(len(s)):
    t = s[:~i]
    dif = set(map(chr,range(ord(s[~i])+1,123))) - set(t)
    if dif:
        ans = t + min(dif)
        break
print(ans)