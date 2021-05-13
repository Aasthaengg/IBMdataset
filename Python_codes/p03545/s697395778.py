A,B,C,D = list(input())
#print(A,B,C,D)

for i in range(2**3):
  argo = ["-","-","-"]
  
  for j in range(3):
    if i>>j & 1:
      argo[3-1-j] = "+"
  #print(argo)
  
  if eval(str(A)+argo[0]+str(B)+argo[1]+str(C)+argo[2]+str(D)) == 7:
    print(str(A)+argo[0]+str(B)+argo[1]+str(C)+argo[2]+str(D)+"=7")
    break