n=int(input())
tarou=0
hanako=0
for i in range(n):
  #print(tarou,hanako)
  t,h=map(str,input().split())
  if t==h:
    tarou+=1
    hanako+=1
  elif (t>h)==True:
    tarou+=3
  else:
    hanako+=3

print(tarou,hanako)
