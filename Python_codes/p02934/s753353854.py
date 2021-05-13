n=int(input())
a=list(map(int,input().split()))
bunsi=1
for i in range(n):
  bunsi*=a[i]

bunbo=0
for i in range(n):
  bunbo += bunsi // a[i]
  
print(bunsi/bunbo)