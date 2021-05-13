A=input()
B=input()
C=input()
X=input()
A=int(A)
B=int(B)
C=int(C)
X=int(X)
count=0
for i in range(A+1):
  for j in range(B+1):
    for k in range(C+1):
      if 500*i+100*j+50*k==X:
        count=count+1
print(count)