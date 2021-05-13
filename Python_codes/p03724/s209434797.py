n,m=map(int,input().split())
cnt=[0for i in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  cnt[a-1]+=1
  cnt[b-1]+=1
print('YES' if all(i%2==0 for i in cnt) else 'NO')