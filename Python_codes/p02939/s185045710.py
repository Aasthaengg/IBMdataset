s = input()
ansL = [s[0]]
ans = ""
for i in s[1:]:
    ans += i
    if ansL[-1] != ans:
        ansL.append(ans)
        ans = ""
print(len(ansL))
