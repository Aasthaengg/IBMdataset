n,k=map(int,input().split())
a = list(map(int,input().split()))
minus = [0]+[abs(a[i]) for i in range(n) if a[i] < 0][::-1]

plus = [0]+[a[i] for i in range(n) if a[i] >= 0]

min_ = 10**18

if len(plus) == 1:
  print(minus[k])
elif len(minus) == 1:
  print(plus[k])
else:
  for i in range(min(k+1, len(plus))):
    if k-i < len(minus):
      min_ = min(min_, 2*plus[i]+minus[k-i], plus[i]+2*minus[k-i])
  print(min_)
  
