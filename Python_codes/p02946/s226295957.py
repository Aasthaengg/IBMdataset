k,x = map(int,input().split())
ans = [x]
for i in range (k-1):
  ans.append(x+i+1)
  ans.append(x-i-1)
ans.sort()
for j in range(len(ans)):
  print(ans[j],end=" ")