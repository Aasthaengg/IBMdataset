s = input()

ans = 999
for i,j,k in zip(s, s[1:], s[2:]):
    diff = abs(753 - int(i+j+k))
    ans = min(ans, diff)

print(ans)