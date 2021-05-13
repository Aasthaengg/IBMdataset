N = int(input())
K = int(input())
total = 1
for i in range(N):
  if total*2 < total+K:
    total*=2
  else:
    total+=K
print(total)