import sys
A,B,C,D = map(int,input().split())
while True:
  C -= B
  if C <= 0:
    print("Yes")
    sys.exit()
  A -= D
  if A <= 0:
    print("No")
    sys.exit()