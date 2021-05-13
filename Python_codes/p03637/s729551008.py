N = int(input())
a = list(map(int, input().split()))

num2 = 0
num4 = 0
for i in range(N):
  if a[i] % 4 == 0:
    num4 += 1
  elif a[i] % 2 == 0:
    num2 += 1

if num4 >= N // 2 or num4*2 + num2 >= N:
  print('Yes')
else:
  print('No')