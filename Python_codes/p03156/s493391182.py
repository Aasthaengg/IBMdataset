n = int(input())
a,b = map(int, input().split())
p = list(map(int, input().split()))
A,B,C = 0,0,0
for v in p:
  if v <= a: A += 1
  elif v <= b: B += 1
  else: C += 1
print(min(A,B,C))