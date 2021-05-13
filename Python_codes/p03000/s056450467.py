n,x =map(int, input().split())
l = list(map(int, input().split()))
d = [0]*(n+1)
for i in range(len(l)):
  d[i+1] = d[i]+l[i]
cnt=0
for i in d:
  if i <= x:
    cnt+=1
print(cnt)