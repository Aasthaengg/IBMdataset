a,b,k = map(int, input().split())

A = list(range(a,min(a+k,b+1)))
B = list(range(max(a,b-k+1),b+1))
ans = list(set(A)|set(B))
ans.sort()
for i in range(len(ans)):
  print(ans[i])