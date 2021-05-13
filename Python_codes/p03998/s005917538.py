s =[list(input()) for i in range(3)]
i = 0;j =0;
while len(s):
  if s[i] ==[]:
    print("A" if i==0 else "B" if i==1 else "C")
    break
  if s[i][j] =="a":
    del s[i][j]
    i =0
  elif s[i][j] =="b":
    del s[i][j]
    i =1
  else:
    del s[i][j]
    i =2