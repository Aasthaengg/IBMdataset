count = 0
n,m = map(int,input().split())
for i in range(2,n+1):
  for j in range(2,m+1):
    count += 1
print(count)