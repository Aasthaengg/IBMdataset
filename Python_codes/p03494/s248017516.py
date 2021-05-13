N=int(input())
x=list(map(int,input().split()))

count=[0]*N

for i in range(N):
  while x[i]%2==0:
    x[i]/=2
    count[i]+=1
    
print(min(count))