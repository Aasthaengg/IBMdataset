n, m, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
 
a_sum=[0]
for i in range(n):
  a_sum.append(a[i]+a_sum[i])
  
b_sum=[0]
for i in range(m):
  b_sum.append(b[i]+b_sum[i])
  
ans, j = 0, m
for i in range(n+1):
  if a_sum[i]>k:
    break
  while a_sum[i] + b_sum[j] > k and j>0:
    j-=1
  if a_sum[i]+b_sum[j]<=k:
    ans=max(ans, i+j)
print(ans)