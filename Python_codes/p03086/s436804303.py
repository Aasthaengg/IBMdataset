# B - ATCoder
S = input()
ans = 0
tmp = 0
for i in range(len(S)):
    if S[i] in ['A','C','G','T']:
        tmp += 1
    else:
        ans = max(ans,tmp)
        tmp = 0
ans = max(ans,tmp)
print(ans)