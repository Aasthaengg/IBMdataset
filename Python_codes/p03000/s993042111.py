n,x=map(int,input().split())
l=list(map(int,input().split()))
i=z=0
while z<=x and i<n:
    z+=l[i]
    i+=1
if z<=x:
    i+=1
print(i)