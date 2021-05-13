A, B = map(int, input().split())

ca_min = 100*A / 8
ca_max = 100*(A+1) / 8

cb_min = 10*B
cb_max = 10*(B+1)

# ca_min<= ca < ca_max
# cb_min<= cb < cb_max

AA = []
BB = []

for i in range(1, 1001):
  if ca_min<= int(i) < ca_max:
    AA.append(int(i))

for i in range(1, 1001):
  if cb_min<= int(i) < cb_max:
    BB.append(int(i))

CC = set(AA) & set(BB)

if CC == set():
  print(-1)
else:
  print(min(CC))


