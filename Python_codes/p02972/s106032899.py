n = int(input())
a = list(map(int, input().split()))


ans = set()
for i in range(n-1, -1, -1):
  for j in range(i+1,n+1,i+1):
    if j in ans:
      a[i] += 1
  if a[i]%2 == 1:
    ans.add(i+1)
print (len(ans))
print (*ans)