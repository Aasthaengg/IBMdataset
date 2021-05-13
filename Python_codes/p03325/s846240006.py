N=int(input())
a=list(map(int,input().split()))
count=0
for i in range(N):
  while True :
    if a[i]%2!=0 :
      break
    count+=1
    a[i]/=2
print(count)