n, k = map(int, input().split())

q_1 = n % k
q_2 = k - q_1
if q_1 < q_2:
  print(q_1)
else:
  print(q_2)