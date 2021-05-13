A, B, C, D = map(int, input().split())

while A > 0 or C > 0:
  C -= B
  if C <= 0:
    print("Yes")
    break
  else:
    pass
  A -= D
  if A <= 0:
    print("No")
    break
  else:
    pass