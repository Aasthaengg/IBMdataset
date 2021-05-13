N,M = map(int,input().split())
a =[0]*M
b =[0]*M

ans = [0]*N

for i in range(M):
  a[i],b[i] = map(int,input().split())

for _ in range(M):
  ans[a[_]-1]+=1
  ans[b[_]-1]+=1

for j in range(N):
  print(ans[j])