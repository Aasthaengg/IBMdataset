n,k = map(int,input().split())
lis = list(map(int,input().split()))
ans = 0
for i in range(n-1):
  if lis[i] + lis[i+1] > k:
    num = lis[i+1]+lis[i] -k
    ans += num
    if num >= lis[i+1]:
      num -= lis[i+1]
      lis[i+1] = 0
      lis[i] -= num
    else:
      lis[i+1] -= num
print(ans)
