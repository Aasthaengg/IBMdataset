a,b,c=map(int,input().split())
residue= a-b
res = c- residue
if res <=0:
  print(0)
else:
  print(res)