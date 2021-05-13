n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
count = 0
back = 0
for i in range(0, n):
  count += b[a[i]-1]
  if back+1 == a[i] and back != 0:
    count += c[a[i]-2]
  back = a[i]
print(count)