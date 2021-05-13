n,m=map(int,input().split())
s1=[input() for _ in range(n)]
s2=[input() for _ in range(m)]
ans='No'
for i in range(n-m+1):
  for j in range(n-m+1):
    flg=0
    for k in range(m):
      if s1[j+k][i:i+m]==s2[k]:
        flg+=1
    if flg==m:
      ans='Yes'
print(ans)