A,B,C,D = map(int,input().split())
for cnt in range(100):
  C = C - B
  if C <= 0:
    print("Yes")
    break
  A = A - D
  if A <= 0:
    print("No")
    break