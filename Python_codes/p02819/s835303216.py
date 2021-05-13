x=int(input())

era=[1]*(10**6+1)
era[0]=0
era[1]=0
k=2
while k<10**6+1:
  if era[k]==1:
    for i in range(2*k,10**6+1,k):
      era[i]=0
  if k==2:
    k+=1
  else:
    k+=2
for i in range(x,10**6+1):
  if era[i]==1:
    print(i)
    break