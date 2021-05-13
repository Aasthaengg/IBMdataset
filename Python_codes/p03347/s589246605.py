n=int(input())
a=[int(input()) for _ in range(n)]
for i,x in enumerate(a):
  if x<=i:
    pass
  else:
    print(-1)
    exit()
ans=0
pre=0
for x in a[::-1]:
  if x>=pre:
    ans+=x
  if x<pre-1:
    print(-1)
    exit()
  pre=x
print(ans)
