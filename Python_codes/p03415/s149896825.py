ss = open(0).read().splitlines()

ans = ''
for i,s in enumerate(ss):
    ans += s[i]
print(ans)