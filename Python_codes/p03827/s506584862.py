n,s = open(0).readlines()

tmp = 0
ans = 0

for c in s:
    if c=='I':
        tmp += 1
    else:
        tmp -= 1
    ans = max(tmp, ans)

print(ans)