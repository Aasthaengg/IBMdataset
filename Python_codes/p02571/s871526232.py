s = input()
t = input()

lens = len(s)
lent = len(t)
ans = 10000
for i in range(lens-lent+1):
    tmp = 0
    for j in range(lent):
        if(s[i+j] != t[j]):
            tmp += 1
    ans = min(tmp,ans)

print(ans)
