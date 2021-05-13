S = input()
pres = S[0]
ans = 0
for s in S[1:]:
    if pres == s:
        continue
    else:
        pres = s
        ans += 1
print(ans)
