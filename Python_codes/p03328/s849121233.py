d=[i*(i+1)//2 for i in range(1,1000)]
a,b=map(int,input().split())
for j in range(998):
  if d[j+1]-d[j]==b-a:
    print(d[j]-a)
    break