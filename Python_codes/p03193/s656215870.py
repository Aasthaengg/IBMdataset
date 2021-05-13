n,h,w=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
z=0
for t in ab:
    if t[0]>=h and t[1]>=w:
        z+=1
print(z)