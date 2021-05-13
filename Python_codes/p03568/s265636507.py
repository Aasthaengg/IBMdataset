import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
res = 1
for x in a:
  if x % 2 == 0: res *= 2
print(pow(3, N) - res)