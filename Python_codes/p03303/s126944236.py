s=input()
w=int(input())
ans=s[0]
for i in range(1,len(s)):
    if i%w==0:
        ans=ans+s[i]
print(ans)
