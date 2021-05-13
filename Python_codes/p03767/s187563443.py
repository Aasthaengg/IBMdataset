n=int(input())
*a,=map(int,input().split())
a.sort()
a.reverse()
ans=0
for i in range(n):
  ans+=a[i*2+1]
print(ans)