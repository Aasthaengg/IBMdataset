n = input()
if len(n)==1:
  print(n)
else:
  nines = 1
  for i in range(1,len(n)):
    if n[i]!="9":
      nines = 0
  if nines == 1:
    print((len(n)-1)*9+int(n[0]))
  else:
    print((len(n)-1)*9+(int(n[0])-1))