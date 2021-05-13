n=int(input())
a=[list(map(int,input().split())) for i in range(2)]

best=[]

for i in range(n):
  s=sum(a[0][0:i+1]+a[1][i:])
  best.append(s)
  
print(max(best))