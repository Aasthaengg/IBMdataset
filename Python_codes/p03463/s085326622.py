N, A, B = map(int, input().split())
while True:
  if abs(B-A)%2 == 1:
    print("Borys")
    break
  elif abs(B-A)%2 == 0:
    print("Alice")
    break