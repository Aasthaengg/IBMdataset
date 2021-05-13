s = input()
t = input()
ans=0
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    else:
        ans+=1
print(ans)