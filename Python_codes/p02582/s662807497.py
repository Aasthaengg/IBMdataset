s = str(input())
ans = 0
tmp = 0
for i in range(len(s)):
    if(s[i] == 'R'):
        tmp += 1
    else:
        ans = max(tmp,ans)
        tmp = 0

ans = max(tmp,ans)
print(ans)