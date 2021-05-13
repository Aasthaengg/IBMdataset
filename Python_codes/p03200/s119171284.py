s=list(input())
cnt=s.count('W')
a=[i for i,x in enumerate(s) if x=='W']
ans=0
for i in range(cnt):
  ans+=a[i]-i
print(ans)