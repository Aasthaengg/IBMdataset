n,m = map(int,input().split())
array = [0]*m

for i in range(n):
  k = list(map(int,input().split()))
  for j in range(1,k[0]+1):
    array[k[j]-1] += 1

print(array.count(n))
