i,j,k = map(int,input().split())
count = 0
for t in range(i):
  tmp = list(map(int,input().split()))
  if tmp[0] >= j and tmp[1] >= k:
    count += 1
print(count)