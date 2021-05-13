import itertools
h,w,k=map(int,input().split())
lst=[list(input()) for i in range(h)]
lst2=[lst[i] for i in range(h)]

pin=0
for i in range(h):
  pin+=lst[i].count('#')

ans=0

for hei in itertools.product(range(2),repeat=h):
  for wid in itertools.product(range(2),repeat=w):
    cnt=0
    for i in range(h):
      for j in range(w):
        if hei[i]==1 and wid[j]==1 and lst[i][j]=="#":
          cnt+=1
    
    if cnt==k:
      ans+=1

    
print(ans)