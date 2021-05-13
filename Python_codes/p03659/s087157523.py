N = int(input())
a = list(map(int,input().split()))
a_sum = [0]
tmp = 0
for i in range(1,N+1):
  tmp = a_sum[i-1] + a[i-1]
  a_sum.append(tmp)
ans = 10**30
x,y = 0,0
for i in range(1,N):
  x = a_sum[i]
  y = a_sum[N] - x
  ans = min(ans,abs(x-y))
print(ans)