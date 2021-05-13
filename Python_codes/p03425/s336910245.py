M,A,R,C,H=list(),list(),list(),list(),list()
N=int(input())
for i in range(N):
  S=input()
  if S[0]=="M":
    M.append(S)
  elif S[0]=="A":
    A.append(S)
  elif S[0]=="R":
    R.append(S)
  elif S[0]=="C":
    C.append(S)
  elif S[0]=="H":
    H.append(S)
a=len(M)
b=len(A)
c=len(R)
d=len(C)
e=len(H)
print(a*b*c+a*b*d+a*b*e+a*c*d+a*c*e+a*d*e+b*c*d+b*c*e+b*d*e+c*d*e)