a,b,x = map(int,input().split())
alpha = 0
beta = 0
if a-1 == -1:
  alpha = 0
else:
  alpha = ((a-1)//x)+1
beta = (b//x)+1
print(beta-alpha)