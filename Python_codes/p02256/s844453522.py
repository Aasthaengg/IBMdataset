s = input().split()
A = int(s[0])
B = int(s[1])

if A < B:
  v = B
  B = A
  A = v

R = A % B
while R !=0:
  A = B
  B = R
  R = A % B
print(B)
