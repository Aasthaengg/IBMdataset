N=int(input())
H=list(map(int,input().split()))

count = 0
MAX=0
for i in range(1,N):
  if H[i]<=H[i-1]:count += 1
  else:count = 0
  if MAX < count:MAX=count
print(MAX)