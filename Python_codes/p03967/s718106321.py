N=input()
X=len(N)
A=[]
for i in range(X):
  A.append(N[i])



rock=0
paper=0
win=0
lose=0
for i in range (X):
  if A[i]=="g":
    if rock>=paper+1:
      win+=1
      paper+=1
    else:
      rock+=1
  else:
    if rock>=paper+1:
      paper+=1
    else:
      rock+=1
      lose+=1


print(win-lose)
