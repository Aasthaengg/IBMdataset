n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
sum = 0
for i in range(len(a)):
  sum += b[a[i]-1]
  if i>0:
    if a[i]-1 == a[i-1]:
      sum += c[a[i-1]-1]
print(sum)