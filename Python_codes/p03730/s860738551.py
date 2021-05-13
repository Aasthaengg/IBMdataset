A, B, C = map(int,input().split())

counter = 1
possible_remainders = []


while counter >= 0:
  remainder = (A*counter)%B
  if remainder in possible_remainders:
    break
  else:
    possible_remainders.append(remainder)
    counter += 1

if C in possible_remainders:
  print("YES")
else:
  print("NO")