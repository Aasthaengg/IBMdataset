a,b,k=map(int,input().split())
i=min(a,b)+1
while(k):
  i-=1
  if max(a%i,b%i)==0:
    k-=1
print(i)