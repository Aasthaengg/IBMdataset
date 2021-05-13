a,b = map(int,input().split())
 
ans = a-1
 
for i in range(1,b+1):
  if a==i:
    ans = ans+1
    break
print(ans)