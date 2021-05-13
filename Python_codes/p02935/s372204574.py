N=int(input())
V=list(map(int,input().split()))
for i in range(N-2):
    V=sorted(V)
    W=(V[0]+V[1])/2
    V=V[2:]
    V.append(W)
print((V[0]+V[1])/2)