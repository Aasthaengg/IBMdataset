n=int(input())
arr=[int(input()) for _ in range(n)]
pos=[0]*(n+1)
for i in range(n):
  pos[arr[i]]=i
cnt=[0]*(n+1)
cnt[1]=1
for i in range(2,n+1):
  if pos[i-1]<pos[i]:
    cnt[i]=cnt[i-1]+1
  else:
    cnt[i]=1
print(n-max(cnt))