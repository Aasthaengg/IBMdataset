n,m=map(int,input().split())
a=list(map(int, input().split()))

sum_a = sum(a)
if n - sum_a <= -1:
  print('-1')
else:
  print(n - sum_a)