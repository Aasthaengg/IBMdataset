r,d,x0=map(int,input().split())
list=[x0]
for i in range(1,11):
  list.append(r*list[i-1]-d)
list.remove(x0)
for x in range(10):
  print(list[x])