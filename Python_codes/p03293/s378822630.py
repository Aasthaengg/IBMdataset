s=input()
t=input()

def rote(st):
  return st[1:]+st[0]
ans="No"
for i in range(len(s)):
  if s==t:
    ans="Yes"
    break
  t=rote(t)

  
print(ans)