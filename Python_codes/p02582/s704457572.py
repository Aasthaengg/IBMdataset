s=input()
 
if s in ["RRR"]:
  print(3)
elif s in ["RRS","SRR"]:
  print(2)
elif s in ["RSS","SRS","SSR","RSR"]:
  print(1)
else:
  print(0)