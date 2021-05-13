N = int(input())
c = 0
ans = 1

while (c+1)**2<=N:
  ans = (c+1)**2
  c+=1
  
print(ans)