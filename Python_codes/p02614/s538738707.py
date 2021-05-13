import itertools

h,w,k=map(int,input().split())
c=[list(input()) for i in range(h)]
ans=0
for filter_row in range(2**h):
  for filter_col in range(2**w):
    cnt=0
    for i in range(h):
      for j in range(w):
        if (filter_row>>i&1)!=0 and (filter_col>>j&1)!=0 and c[i][j]=='#':
          cnt+=1
    if cnt==k:
      ans+=1
print(ans)