n = int(input())
k = int(input())
i = 1
while n>0:
  if (i*2-i) > k: i+=k
  else: i*=2
  n-=1
print(i)