S = input()
ans = 1
tmp = S[0]
flg = False
for i in range(1,len(S)):
    if flg:
        tmp += S[i]
        ans += 1
        flg = False
        continue
    if S[i] != tmp:
        tmp = S[i]
        ans += 1
    else:
        flg = True
print(ans)
