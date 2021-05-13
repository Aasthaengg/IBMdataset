N,K=[int(x) for x in str(input()).split()]
A=[int(x) for x in str(input()).split()]
bA=[]

Am=max(A)

lAm=len(bin(Am))-2

k=bin(K)[2:]
lK=len(bin(K))-2




ANS=[[-1 for i in range(2)] for j in range(41)]




for i in range(N):
  X=bin(A[i])[2:]
  for j in range(max(lAm,lK)-len(X)):
    X="0"+X
  bA.append(X)

for j in range(max(lAm,lK)-len(k)):
  k="0"+k




def opt(a,index,counter):
  if ANS[index][counter]==-1:
    if index<a:
      if counter==1:
        z=0
        o=0
        for i in range(N):
          if bA[i][index]=="1":
            o+=1
          else:
            z+=1

        temp=k[index]
        if temp=="1":
          t1=o*pow(2,a-index-1) + opt(a,index+1,0)

          t2=z*pow(2,a-index-1) + opt(a,index+1,1)
          ANS[index][counter]=max(t1,t2)
        else:
          ANS[index][counter]=o*pow(2,a-index-1) + opt(a,index+1,1)
      elif counter==0:
        z=0
        o=0
        for i in range(N):
          if bA[i][index]=="1":
            o+=1
          else:
            z+=1
        ANS[index][counter]=max(o,z)*pow(2,a-index-1) + opt(a,index+1,0)
    else:
      ANS[index][counter]=0
  
  return ANS[index][counter]


print(opt(max(lAm,lK),0,1))















