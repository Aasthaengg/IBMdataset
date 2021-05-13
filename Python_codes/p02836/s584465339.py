s=input()
s1=s[:len(s)//2]
s2=s[len(s)//2:][::-1]
ans=0
for i in range(len(s)//2):
    if s1[i]!=s2[i]:
        ans+=1
print(ans)