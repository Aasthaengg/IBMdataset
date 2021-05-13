l,r=map(int,input().split())
mini=2019
L=l
R=r+1 if r-l<2019*2 else l+2019+1
for i in range(L,R):
    for j in range(i+1,R):
        mini=min(mini,i*j%2019)
print(mini)