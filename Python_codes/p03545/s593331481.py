S=input()
A=int(S[0])
B=int(S[1])
C=int(S[2])
D=int(S[3])
ans=""
for x in [1,-1]:
  for y in [1,-1]:
    for z in [1,-1]:
      if A+B*x+C*y+D*z==7:
        if x==1:
          sx="+"
        else:
          sx="-"
        if y==1:
          sy="+"
        else:
          sy="-"
        if z==1:
          sz="+"
        else:
          sz="-"
        ans=str(A)+sx+str(B)+sy+str(C)+sz+str(D)+"=7"
print(ans)