s=input()
ans=''
for i in range(len(s)):ans=ans+(''if i%2 else s[i])
print(ans)