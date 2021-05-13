num=int(input())
D=list(map(int,input().split()))
val=0
for i in range (0,len(D)):
  for j in range (i+1,len(D)):
    val+=D[i]*D[j]
print(val)