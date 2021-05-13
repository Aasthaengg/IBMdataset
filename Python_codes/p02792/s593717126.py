n=int(input())
c=[0 for i in range(100)]

for i in range(n+1):
  s=str(i)
  if s[-1]==0:
    continue
  c[int(s[0])*10+int(s[-1])]+=1

ans=0
for i in range(1,10):
  for j in range(1,10):
    ans+=c[i*10+j]*c[i+j*10]
print(ans)