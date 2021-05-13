n = int(input())
P = [int(x) for x in input().split()]
count = 0

for i in range(n-2):
  if (P[i] < P[i+1]) and (P[i+1] < P[i+2]):
    count += 1
  elif (P[i] > P[i+1]) and (P[i+1] > P[i+2]):
    count += 1

print(count)