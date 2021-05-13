n,s= map(int,input().split())
min = s-n+1
max =s+n
if(s-n<-1000000): min = -1000000
if((s+n)>1000001): max = 1000001
for i in range(min,max):
  print(i,end=" ")