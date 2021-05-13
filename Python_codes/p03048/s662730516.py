r,g,b,n= map(int, input().split())
[r,g,b] = sorted([r,g,b])
cnt = 0
for i in range(n//b+1):
  for j in range((n-b*i)//g+1):
    if n>=b*i+g*j and (n-(b*i+g*j))%r==0: cnt += 1
print(cnt)