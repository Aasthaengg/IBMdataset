#CADDi 2018 for Beginners b
n,h,w=map(int,input().split())
ans=0
for i in range(n):
    tate,yoko=map(int,input().split())
    if tate>=h and yoko>=w:
        ans+=1
print(ans)