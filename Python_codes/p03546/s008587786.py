h,w=map(int,input().split())
c=[list(map(int,input().split())) for i in range(10)]
a=[list(map(int,input().split())) for i in range(h)]

for k in range(10):
  for i in range(10):
    for j in range(10):
      c[i][j]=min(c[i][j],c[i][k]+c[k][j])

spell=0
for wist in a:
  for val in wist:
    if val==-1:continue
    spell+=c[val][1]
print(spell)