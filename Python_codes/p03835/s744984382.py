K,S=map(int,input().split())
R=range(0,K+1)

W=0
for X in R:
    for Y in R:
        Z=S-(X+Y)
        W+=(0<=Z<=K)
print(W)
