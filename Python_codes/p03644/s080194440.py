N = int(input())
list2 = []

list1 =[int(i) for i in range(1,N+1)]
for i in range(N):
  list2.append([i, list1[i]])

for i in range(N):
  if len(list2) == 1:
    ans = list2[0][0]
    print(ans+1)  
    break
  
    
  for a in list2:
    
    if a[1] % 2 != 0:
      list2.remove(a)

  for j in range(len(list2)):
    list2[j][1] = list2[j][1]/2