n = int(input())
list_a = list(map(int, input().split()))

max_a = [-1, -1]
for i in range(n):
  if abs(list_a[i]) > max_a[1]:
    max_a = [i, abs(list_a[i])]

print(2 * n - 1)
for i in range(n):
  print(max_a[0]+1, i+1)
if list_a[max_a[0]] > 0:
  for i in range(n-1):
    print(i+1, i+2)
else:
  for i in range(n-1)[::-1]:
    print(i+2, i+1)