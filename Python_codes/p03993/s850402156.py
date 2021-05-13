N=int(input())
a=[0]+list(map(int,input().split()))
cnt=0

for i in range(1,N+1):
  if i== a[a[i]]:
    cnt +=1
    
print(cnt//2)