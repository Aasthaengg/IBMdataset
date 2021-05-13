N=int(input())
a=list(map(int, input().split(" ")))

count=0

for i in range(len(a)):
  if a[i]-1>i and i==a[a[i]-1]-1:
    count=count+1
    
print(count)