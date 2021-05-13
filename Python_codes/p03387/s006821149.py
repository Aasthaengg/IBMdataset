abc = list(map(int,input().split()))
abc.sort()

A=abc[0]
B=abc[1]
C=abc[2]

if (B-A)%2 == 0:
  print(C-B+(B-A)//2)
else:
  print(C-B+(B-A+3)//2)