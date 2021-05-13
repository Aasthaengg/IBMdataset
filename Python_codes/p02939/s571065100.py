s=input()
ans=0
k=""
hantei=""
for i in s:
  k+=i
  if k!=hantei:
    hantei=k
    k=""
    ans+=1
print(ans)