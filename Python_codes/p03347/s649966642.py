n=int(input())
a=[-1]+[int(input()) for _ in range(n)]
for i,j in zip(a[:n],a[1:]):
  if i<j-1:
    print(-1)
    exit()
ans=0
for i,j in zip(a[1:n],a[2:]):
  if j-i==1:ans+=1
  else:ans+=j
print(ans)