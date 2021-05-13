s=input()
p=['+','-']
for i in range(8):
  t=s
  for j in range(3):
    t=t[:3-j]+p[(i>>j)&1]+t[3-j:]
  if eval(t)==7:
    print(t+'=7')
    exit()