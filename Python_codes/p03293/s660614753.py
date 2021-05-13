s=input()
t=input()
st=s
ans="No"

for i in range(len(s)):
  st=st[-1]+st[:-1]
  if st==t:
    ans="Yes"
    
print(ans)