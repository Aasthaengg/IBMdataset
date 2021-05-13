n=int(input())
cnt=0
i=1
while i<=n:
  c=0
  for j in range(1,i+1):
    if i%j==0:
      c+=1
  if c==8:
    cnt+=1
  i+=2
print(cnt)