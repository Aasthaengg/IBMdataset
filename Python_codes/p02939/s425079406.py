s = input()

l = len(s)
ans = 1
tmp = s[0]
nxt = ""
for i in range(1,l):
    nxt += s[i]    
    if tmp == nxt:
        continue
    else:
        ans += 1
        tmp = nxt
        nxt = ""

print(ans)