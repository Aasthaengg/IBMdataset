n = int(input())
xs = [int(x) for x in input().split()]

xs[0] -= 1
for i in range(1,n):
  if xs[i-1] <= xs[i] - 1:
    xs[i] -= 1

print('Yes' if sorted(xs) == xs else 'No')