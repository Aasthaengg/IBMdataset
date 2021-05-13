import sys
n = int(input())
a = sorted(list(map(int, input().split())))
for i in range(n):
  if a[i] != (2 * ((i + 2 - n % 2) // 2) + n % 2 - 1):
    print(0)
    sys.exit()
print(pow(2, n // 2, 1000000007))
