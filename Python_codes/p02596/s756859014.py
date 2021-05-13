k=int(input())
a=0
for i in range(k):
  a+=7*pow(10,i,k)
  a%=k
  if a==0:
    print(i+1)
    exit()
print(-1)