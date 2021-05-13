n = int(input())
cou = 0
for i in range(1,n+1):
  i = str(i)
  if i[0]!="0" and i[-1]!="0":
    if int(i[0])>int(i[-1]):
      cou +=  (10**(len(i)-1)-1)//9
    elif int(i[0])<int(i[-1]):
      cou += (10**(len(i)-2)-1)//9
  #print(i,cou)

cou *= 2
    
l = [0 for i in range(9)]
for i in range(1,n+1):
  i = str(i)
  if i[0]==i[-1]:
    l[int(i[0])-1] += 1
l1 = [i*i for i in l]
print(sum(l1)+cou)