A,B = map(int,input().split())
ans = 0

for a in range(A,B+1):
  a = list(str(a))
  if a[0]==a[4] and a[1]==a[3]:
    ans+=1
    
print(ans)