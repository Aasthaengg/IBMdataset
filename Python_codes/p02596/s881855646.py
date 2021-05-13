K=int(input())
a=[0]*1000001
a[1]=7%K
for i in range(2,K+1):
  a[i]=(a[i-1]*10+7)%K
for i in range(1,K+1):
  if a[i]==0:
    print(i)
    exit()
print(-1)
