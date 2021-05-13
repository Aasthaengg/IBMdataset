N,K=map(int,input().split())
k = 0
res = 0
flag = True
for i in range(1,N+1):
  flag = True
  mid = 1/N
  k = i
  if k >=K:
    pass
  else:
    while k<K:
      mid = mid*0.5
      k = k*2
  res += mid
print(res)