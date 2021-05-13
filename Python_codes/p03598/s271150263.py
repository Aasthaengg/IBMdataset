n=int(input())
k=int(input())
x=list(map(int,input().split()))
total=0
for i in range(n):
  if x[i]<=k-x[i]:
    total+=x[i]
  else:
    total+=k-x[i]
print(total*2)