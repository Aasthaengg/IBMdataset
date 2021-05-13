n=int(input())
k=int(input())
temp=1
for i in range(0,n):
  temp=min(temp+k,temp*2)
print(temp)