input_val = input().split()
A=int(input_val[0])
B=int(input_val[1])
if B%A==0:
  print(B+A)
else:
  print(B-A)