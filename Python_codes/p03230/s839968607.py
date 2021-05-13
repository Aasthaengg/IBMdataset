n=int(input())
if not ((1+(1+8*n)**0.5)/2).is_integer():
  print('No')
else:
  k=int((1+(1+8*n)**0.5)//2)
  ans=[[] for _ in range(k)]
  cnt=1
  for i in range(k):
    for j in range(i+1,k):
      ans[i].append(cnt)
      ans[j].append(cnt)
      cnt+=1
  print('Yes')
  print(k)
  for i in range(k):
    print(k-1,*ans[i])