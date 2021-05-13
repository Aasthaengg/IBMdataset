n = int(input())
a=list(map(int,input().split()))
s = sum(a)
s_tmp = 0
min_ = 10**18
for i in range(n-1):
  s_tmp += a[i]
  min_ = min(min_, abs(s_tmp-(s-s_tmp)))
print(min_)