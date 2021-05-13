N = int(input())
MM = input().split()
count = 0
list1 =[]
for i in MM:
  a = int(i)
  list1.append(a)
list2 = sorted(list1)
for i,j in zip(list1,list2):
  
  if i != j:
    
    count +=1
if count >2:
  print('NO')
else:
  print('YES')