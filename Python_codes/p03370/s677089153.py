import math

N, X = map(int, input().split())
num = 0
n = []
while num < N :
  n.append(int(input()))
  num += 1
print(math.floor((X - sum(n)) / min(n)) + N)