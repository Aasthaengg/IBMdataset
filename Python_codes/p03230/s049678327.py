n=int(input())
nn=int((n*2)**0.5)
if n*2!=nn*(nn+1):
  print("No")
else:
  print("Yes")
  print(nn+1)
  Ans=[[0]*nn for _ in range(nn+1)]
  for i in range(nn):
    for j in range(nn-i):
      Ans[i][i+j]+=nn*i-i*(i-1)//2+j+1
      Ans[i+j+1][i]+=nn*i-i*(i-1)//2+j+1
  for a in Ans:
    print(nn,*a)