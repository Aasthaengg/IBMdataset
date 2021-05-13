S = input()

if len(S) == 1:
    print(1)
    exit()

ans = 1
tmp1 = S[0]
tmp2 = ""

for i in range(1,len(S)):
    tmp2 += S[i]
    if tmp1 == tmp2:
        continue
    else:
        ans += 1
        tmp1 = tmp2
        tmp2 = ""

print(ans)