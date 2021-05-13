th,ta,ah,aa = map(int, input().split())
while th > 0 or ah > 0:
  ah -= ta
  if ah <= 0:
    break
  th -= aa
print("Yes" if th > 0 else "No")