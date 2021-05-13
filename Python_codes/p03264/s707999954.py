K = int(input())
cnt = 0

for i1 in range(1,K+1):
  for i2 in range(i1+1, K+1):
    if i1%2 != 0 and i2%2 == 0:
      cnt = cnt+1
    elif i1%2 ==0 and i2%2 != 0:
      cnt = cnt+1
      
print(cnt)