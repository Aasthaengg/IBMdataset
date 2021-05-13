A,B,C,D = input()
op = ["+","-"]

for op1 in op:
  for op2 in op:
    for op3 in op:
      S = A+op1+B+op2+C+op3+D
      if eval(S)==7:
        print(S+"=7")
        exit()