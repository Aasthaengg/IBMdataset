n, *p = map(int, open(0))
q = [0] * -~n
for p in p:
  q[p] = q[p - 1] + 1
print(n - max(q))