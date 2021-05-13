A="CODEFESTIVAL2016"
B=input()
C=0
for a,b in zip(A,B):
  if a==b:
    continue
  else:
    C=C+1
print(C)