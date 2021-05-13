n,m=map(int, input().split())
lamp=[]
for i in range(m):
    lamp.append(list(map(int, input().split())))
p=list(map(int, input().split()))

ans=0

for i in range(2**n):
    All_On=True
    for j in range(m):
        k_on=0
        for k in range(1,lamp[j][0]+1):
            if i>>lamp[j][k]-1 & 1:
                k_on+=1
        if k_on%2!=p[j]:
            All_On=False
            break
    if All_On:
        ans+=1
print(ans)