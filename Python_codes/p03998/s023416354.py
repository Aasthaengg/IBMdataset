lis=[]
ll=["a","b","c"]
for i in range(3):
  lis.append(list(input()))
turn=0
while 1:
  if lis[turn]==[]:
    print(ll[turn].upper())
    break
  turn=ll.index(lis[turn].pop(0))
