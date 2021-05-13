A,B,C,D = map(int,list(input()))

for i in [-1,1]:
  for j in [-1,1]:
    for k in [-1,1]:
      if A + B*i+ C*j + D*k == 7:
        it = "-" if i == -1 else "+"
        jt = "-" if j == -1 else "+"
        kt = "-" if k == -1 else "+"
        print(str(A)+it+str(B)+jt+str(C)+kt+str(D)+"=7")
        exit(0)