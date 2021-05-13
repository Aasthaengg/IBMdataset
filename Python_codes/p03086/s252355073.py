s = str(input())
acgt = ['A','C','G','T']
cnt = 0
ans = 0
for i in range(len(s)):
    if s[i] in acgt:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
ans = max(ans,cnt)
print(ans)