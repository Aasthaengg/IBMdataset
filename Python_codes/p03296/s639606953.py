n = int(input())
l=list(map(int, input().split()))
ans=0
i=0
while i<n-1:
  if l[i]==l[i+1]:
    ans+=1
    i=i+2
  else:
    i+=1
print(ans)