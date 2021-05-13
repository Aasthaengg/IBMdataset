import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
  a[i] ^= a[i - 1]
if a[n - 1] == 0:
  print('Yes')
else:
  print('No')
