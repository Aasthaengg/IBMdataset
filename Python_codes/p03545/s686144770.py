A,B,C,D = map(str,list(input()))

for op1 in ["+","-"]:
  for op2 in ["+","-"]:
    for op3 in ["+","-"]:
      if eval(A+op1+B+op2+C+op3+D) == 7:
        ans = A+op1+B+op2+C+op3+D+"=7"
        break
print(ans)