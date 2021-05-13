n,h,w=map(int,input().split())
ab=[tuple(map(int, input().split())) for i in range(n)]
c=0
for i in ab:
  if i[0] >= h and i[1] >= w:
    c+=1
    
print(c)