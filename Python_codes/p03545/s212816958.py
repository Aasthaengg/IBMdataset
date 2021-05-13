N = input()
N = [int(n) for n in N]
A,B,C,D = N
op =['+','-']
ops = []
for a in op:
  for b in op:
    for c in op:
        ops.append(a + b + c)
        
for op in ops:
  S = "{}{}{}{}{}{}{}".format(A,op[0],B,op[1],C,op[2],D)
  if eval(S) == 7:
    print("{}=7".format(S))
    break