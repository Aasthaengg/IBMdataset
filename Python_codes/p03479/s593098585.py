X,Y=map(int,input().split())

count=0
while(X*(2**count)<=Y):
  count+=1
print(count)