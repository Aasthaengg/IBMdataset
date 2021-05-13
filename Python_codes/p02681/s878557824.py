s=input()
t=input()
ans=0
for i in range(len(s)):
    if s[i]==t[i]:
        ans+=1
if ans==len(s):
    print("Yes")
else:
    print("No")