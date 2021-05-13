n=int(input())
s=input()
ans=0

for i in range(1,n-1):
  cnt=0
  x=list(set(s[:i]))
  y=list(set(s[i:]))
  for j in x:
    if j in y:
      cnt+=1
  if ans<cnt:
    ans=cnt
print(ans)
