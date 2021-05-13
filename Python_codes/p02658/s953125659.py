n = int(input())
a = input().split(" ")
kotae=1
listaa = [int(n) for n in a]
lista = sorted(listaa)
if lista[0]==0:
  print(0)
  exit()
for i in range(n):
  kotae*=lista[i]
  if kotae>10**18:
    kotae=-1
    break
if kotae>10**18:
  kotae=-1
print(kotae)