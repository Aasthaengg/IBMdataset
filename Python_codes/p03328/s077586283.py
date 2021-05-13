x,y=map(int,input().split())
table=[]
a=0
for i in range(1000):
  a+=i
  table.append(a)
print(table[y-x]-y)