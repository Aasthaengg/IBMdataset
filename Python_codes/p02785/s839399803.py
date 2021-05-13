from sys import exit

n, k = map(int, input().split())
if n <= k:
  print(0)
  exit()

h = list(map(int, input().split()))
h.sort()

print(sum(h[:n-k]))