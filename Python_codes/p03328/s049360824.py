a,b=map(int,input().split())
sa=b-a
he=0
for i in range(1,sa):
  he+=i
print(he-a)