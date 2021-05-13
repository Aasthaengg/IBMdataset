input();a=list(map(int,input().split()));c=0
while all(i%2==0 for i in a):
  a=[i/2 for i in a];c+=1
print(c)