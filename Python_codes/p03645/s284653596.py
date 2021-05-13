n,m=map(int,input().split())
arrival=set([])
deperture=set([])
for i in range(m):
    a,b=map(int,input().split())
    if a==1:
        deperture.add(b)
    if b==n:
        arrival.add(a)

if len(arrival&deperture)>=1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")