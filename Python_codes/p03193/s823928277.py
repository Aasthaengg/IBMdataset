n,h,w=map(int,input().split())
a,b=[list(map(int,input().split())) for i in range(n)],0
for i in a:
    b+=(i[0]>=h and i[1]>=w)
print(b)