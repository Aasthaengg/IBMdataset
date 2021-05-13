n=int(input())
a=list(map(int,input().split()))
j=0
x=0
ans=0
for i in range(n):
  while j<n and x|a[j]==x+a[j]:
    x|=a[j]
    j+=1
  ans+=j-i
  x^=a[i]
print(ans)