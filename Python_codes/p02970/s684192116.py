n,k=map(int,input().split())

count=1
for i in range(1,21):
  if n>i*(2*k+1):
    count+=1
print(count)