N = int(input())
lista = list(map(int, input().split()))
lista.sort(reverse= True)

count = 0
area = 1

for i in range(len(lista)- 1):
  if(lista[i] == lista[i+ 1]):
    del lista[i]
    area*= lista[i]
    count+= 1
    if(count == 2):
      break
      
if(count == 2):
  print(area)
else:
  print(0)