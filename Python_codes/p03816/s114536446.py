import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
table = [0] * (max(a) + 1)
for x in a: table[x] += 1
t = 0
for x in table:
  if x > 1: t += x - 1
print(N + (-t // 2) * 2)