N = int(input())
S = ""
if N == 0:
  S = "0"
c = 1
while N != 0:
  if N%(2**c) != 0:
    N -= (-2)**(c-1)
    S = "1" + S
  else:
    S = "0" + S
  c += 1  
print(S)     