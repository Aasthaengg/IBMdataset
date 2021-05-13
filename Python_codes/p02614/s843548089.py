h,w,k=map(int,input().split())
c=[input() for i in range(h)]
ans=0
for i in range(2**h):
  for j in range(2**w):
    cnt=0
    for p in range(h):
      for q in range(w):
        if i&(1<<p) and j&(1<<q):
          if c[p][q]=='#':
            cnt+=1
    if cnt==k:
      ans+=1
print(ans)