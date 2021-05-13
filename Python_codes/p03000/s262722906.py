N,X = map(int, input().split())
L = list(map(int, input().split()))
count = 1
D = 0

for i in range(N):
  D += L[i]
  if D <= X:
    count += 1
  else:
    break

print(count)