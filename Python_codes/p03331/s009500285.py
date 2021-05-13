n=int(input())
min_sum=1000000

for a in range(1,n):
  l_a=str(a)
  l_b=str(n-a)
  
  sum_a=0
  sum_b=0
  for e_a in l_a:
    sum_a+=int(e_a)
  for e_b in l_b:
    sum_b+=int(e_b)
  sum_ab = sum_a+sum_b
  
  if sum_ab<min_sum:
    min_sum=sum_ab
    
print(min_sum)
