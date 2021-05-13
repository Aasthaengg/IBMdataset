n,k = map(int,input().split())
ans = 0
num = n+1
for i in range(1,n+2):
  #i個選ぶとき
  if i>=k:
    ans += num
  num += n-(2*i)
print(ans%(10**9+7))