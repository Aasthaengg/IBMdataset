import sys
input = sys.stdin.readline
N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))
table = [0] * 3
for p in P:
  if p <= A:
    table[0] += 1
  elif A < p <= B:
    table[1] += 1
  else: 
    table[2] += 1
print(min(table))