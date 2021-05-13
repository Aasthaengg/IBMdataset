group_1=[1,3,5,7,8,10,12]
group_2=[4,6,9,11]
group_3=[2]
groups=[group_1,group_2,group_3]

a,b=input().split()

a=int(a)
b=int(b)

for i in range(len(groups)):
  if(a in groups[i] and b in groups[i]):
    print("Yes")
    break
else:
  print("No")