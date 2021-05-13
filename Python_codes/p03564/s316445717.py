N = int(input())
K = int(input())
num = 1
while N>0:
  if num > K:
    num += K
  else:
    num *=2
  N-=1
print(num)