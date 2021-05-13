a,b,c=map(int,input().split())
c-=a
if c<0:
    print("NO")
elif b>=c:
    print("YES")
else:
    print("NO")