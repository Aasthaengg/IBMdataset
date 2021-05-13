a = [str(input()) for i in range(2)]
ans=0
for i in range(len(a[0])):
  if not a[0][i] == a[1][i]:
    ans +=1
    
print(ans)