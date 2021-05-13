import sys
n = int(input())
f = []
p=[]

for i in range(n):
  f.append(list(map(int, input().split())))
for i in range(n):
  p.append(list(map(int, input().split())))

ans=-1*sys.maxsize
for i in range(1, 2**10):
  temp=0
  for shop in range(n):
    cnt=0
    for j in range(10):
      if (i>>j & 1 and f[shop][j] == 1):
        cnt+=1
    temp+=p[shop][cnt]
  ans=max(ans,temp)
print(ans)