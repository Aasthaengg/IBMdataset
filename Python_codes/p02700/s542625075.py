A,B,C,D = map(int,input().split())

while C > 0 and A > 0:
  C -= B
  if C <= 0:
    print("Yes")
    exit()
  A -= D
  if A<= 0:
    print("No")
    exit()