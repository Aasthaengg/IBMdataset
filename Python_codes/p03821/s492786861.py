n=int(input())
c=0
d=[list(map(int,input().split())) for _ in range(n)]
for i in reversed(range(n)):
  a=d[i][0]
  b=d[i][1]
  if (a+c)%b!=0:
    c+=b-(a+c)%b
print(c)