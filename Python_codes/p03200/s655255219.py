s=list(input())
l=[]
ans=0
b=0
for i in range(len(s)):
  if s[i] == "W":
    ans+=b
  else:
    b+=1
print(ans)