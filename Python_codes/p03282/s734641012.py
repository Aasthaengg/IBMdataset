S = input()
K = int(input())
lista = list(S)

flag = 0

if(K<= len(lista)):
  for i in range(K):
    if(lista[i] != "1"):
      flag = 1
      ans = lista[i]
      break
  if(flag == 0):
    print(1)
  else:
    print(ans)

else:
  i = 0
  while True:
    if(lista[i] != "1"):
      print(lista[i])
      break
    i+= 1