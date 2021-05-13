from collections import defaultdict

N=int(input())
a=list(map(int,input().split()))

count=defaultdict(int)
count3200=0
for i in range(N):
  if a[i] < 3200:
    count[a[i] // 400] += 1
  else:
    count3200 += 1
    
print(max(len(count),1),len(count)+count3200)