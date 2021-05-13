N,K=map(int,input().split())
p=N//K
q=N%K
if p==0:
  print(1)
elif q==0:
  print(0)
else:
  print(1)