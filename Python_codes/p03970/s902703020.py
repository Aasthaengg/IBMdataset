a = 'CODEFESTIVAL2016'
b = input()
lista = list(a)
listb = list(b)
count = 0
for i in range(len(lista)):
  if lista[i]!=listb[i]:
    count+=1
print(count)