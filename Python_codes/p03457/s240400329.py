n=int(input())

a,b,c=0,0,0

for i in range(n):
  x,y,z=map(int,input().split())
  dist=abs(b-y)+abs(c-z)
  if dist>x-a or (dist-(x-a))%2==1:
    print('No')
    exit()
    
  else:
    a,b,c=x,y,z
    continue
    
print('Yes')