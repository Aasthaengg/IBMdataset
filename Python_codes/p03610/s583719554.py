s=str(input())
s=list(s)
ans=[]
for i in range(0,len(s)):
  if i%2==0:
    ans.append(s[i])
print("".join(ans))