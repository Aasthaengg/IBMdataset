# solution

x,y,z,k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse = True)
b = sorted(list(map(int, input().split())), reverse = True)
c = sorted(list(map(int, input().split())), reverse = True)
ans = []
for p in range(min(k,len(a))):
  for q in range(min(k,len(b))):
    for r in range(min(k,len(c))):
      if((p+1)*(q+1)*(r+1) > k):
        break
      ans.append(a[p] + b[q] + c[r])
      
ans = sorted(ans, reverse = True)
for i in range(k):
  print(ans[i])