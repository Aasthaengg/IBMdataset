k, x = map(int, input().split())
for i in range(2000001):
  if x - k + 1 <= i - 1000000 <= x + k - 1:
    print(i-1000000,end=" ")