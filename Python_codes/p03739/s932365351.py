def sign(x):
  if x<0:
    return -1
  elif x>0:
    return 1
  else:
    return 0
n = int(input())
a = list(map(int,input().split()))
a_sum_pn = 0
a_sum_np = 0
ans_pn = 0
ans_np = 0
flag = 1
for i in range(n):
  a_sum_pn += a[i]
  a_sum_np += a[i]
  if sign(a_sum_pn) != flag:
    ans_pn += abs(flag-a_sum_pn)
    a_sum_pn = flag
  if sign(a_sum_np) != -flag:
    ans_np += abs(-flag-a_sum_np)
    a_sum_np = -flag
  flag *= -1
print(min(ans_pn,ans_np))
