n=int(input())
p=list(map(int,input().split()))
ans=0
for i in range(n-2):
  b=p[i:i+3]
  if b[1]<max(b) and b[1]>min(b):
    ans+=1
print(ans)