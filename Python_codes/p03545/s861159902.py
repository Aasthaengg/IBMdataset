X = list(map(int,list(input())))

for i in range(2**3+1):
  ans =[X[0]]
  for j in range(3):
    d = X[j+1]*(-1)**((i >>j)&1)
    ans.append(d)
  if sum(ans) == 7:
    for i,a in enumerate(ans):
      if a>=0 and i>0:
        print("+",end="")
      print(a,end="")
    print("=7")
    exit()