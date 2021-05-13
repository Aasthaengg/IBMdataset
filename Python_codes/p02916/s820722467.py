n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
sum = 0

for i in range(len(a)):
  num = a[i]-1
  sum += b[num]
  if i >= 1 and a[i]-a[i-1] == 1:
    tmp = a[i]-2
    sum += c[tmp]
else:
  print(sum)
