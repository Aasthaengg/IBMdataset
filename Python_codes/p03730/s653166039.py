x,y,z=map(int,input().split())
l=[]
for i  in range(1,y+1):
    l.append((x*i)%y)
if(z in l):
    print("YES")
else:
    print("NO")
