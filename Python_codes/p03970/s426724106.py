a=input()
ans=0
correct='CODEFESTIVAL2016'
for i in range(16):
  if a[i]!=correct[i]:
    ans+=1
print(ans)