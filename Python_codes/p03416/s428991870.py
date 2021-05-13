a,b=map(int,input().split())
count=0
for i in range(a,b+1):
  temp=str(i)
  temp=list(temp)
  itemp = temp[::-1]
  if temp==itemp:
    count=count+1
print(count)