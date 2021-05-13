n,x = map(int,input().split())
l_lst = list(map(int,input().split()))
b = 0
sum_l = 0
for l in l_lst:
  b+=1
  sum_l += l
  if sum_l > x:
    break
if sum_l <= x:
  b+=1

print(b)
