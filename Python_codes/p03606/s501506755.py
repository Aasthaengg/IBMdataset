a=int(input())
b=[]
for _ in range(a):
  b.append(list(map(int,input().split())))
ans=0
for i in range(a):
  ans+=b[i][1]-b[i][0]+1
print(ans)
