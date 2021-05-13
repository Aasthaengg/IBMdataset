n = int(input())
original = list(map(int , input().split()))
m = int(input())
total = sum(original)
for i in range(m):
  copy = original[:]
  a = list(map(int , input().split()))
  copy[a[0] - 1] = a[1]
  print(sum(copy))