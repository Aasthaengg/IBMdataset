n,k = map(int,input().split())
m = [0] + list(map(int,input().split()))
p = 1

c = [0] * (n + 1)

q = [1]

while True:
  p = m[p]
  if (c[p] == 1):
    break
  c[p] += 1
  q.append(p)
i = q.index(p)
q1 = q[:i]
q2 = q[i:]
if len(q1) > 0 and k < len(q1):
  print(q1[k])
else: 
  print(q2[(k - len(q)) % len(q2)])