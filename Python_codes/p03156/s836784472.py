n = int(input())
a,b = map(int,input().split())
P = list(map(int,input().split()))
q1 = 0
q2 = 0
q3 = 0
for p in P:
  if p <= a:
    q1 += 1
  elif a < p <= b:
    q2 += 1
  else:
    q3 += 1
print(min(q1,q2,q3))