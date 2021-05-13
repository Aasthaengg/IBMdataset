s = input()
t = input()
ans = len(t)
for i in range(len(s)):
    if len(t)> len(s)-i:
        break
    else:
        cnt=0
        for j in range(len(t)):
            if s[i+j]==t[j]:
                cnt+=1
    ans=min(ans,len(t)-cnt)
print(ans)
