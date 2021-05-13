s=input()
t=input()
ans=len(t)
cnt=0

for _ in range(len(s)):
  if _+len(t)>len(s):
    break
  mj=s[_:_+len(t)]
  for i in range(len(t)):
    if mj[i]!=t[i]:
      cnt += 1
  if ans>cnt:
    ans=cnt
  cnt=0
    
print(ans)