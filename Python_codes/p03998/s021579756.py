A=input()
B=input()
C=input()
moto=A
suji="a"
while True:
  if len(moto)==0:
    if suji=="a":
      print("A")
      exit()
    if suji=="b":
      print("B")
      exit()
    if suji=="c":
      print("C")
      exit()
  s=moto[0]
  if suji=="a":
    A=A[1:]
  if suji=="b":
    B=B[1:]
  if suji=="c":
    C=C[1:]
  if s=="a":
    moto=A
    suji="a"
  if s=="b":
    moto=B
    suji="b"
  if s=="c":
    moto=C
    suji="c"