n=int(input())
a=sorted(list(map(int,input().split())))[::-1]
ans=0
for i in range(n):
  ans+=a[i*2+1]
print(ans)