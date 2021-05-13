s=input()
k=int(input())
if len(s)==1:
  print(k//2)
  exit()
c=1
ans=0
for i in range(1,len(s)):
  if s[i-1]==s[i]:
    c+=1
  else:
    ans+=c//2
    c=1
ans+=c//2
ans*=k
cl=0
i=0
while  i<len(s) and s[-1]==s[i]:
  cl+=1
  i+=1
if i<len(s) and cl%2==1 and c%2==1:
  ans+=k-1
elif cl%2==1 and c%2==1:
  ans+=k//2
print(ans)