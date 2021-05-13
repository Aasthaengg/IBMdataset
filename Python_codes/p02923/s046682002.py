N=int(input())
H=list(map(int,input().split()))[::-1]

P=[0]
for i in range(1,N):
    if H[i-1]<=H[i]:
        P.append(P[-1]+1)
    else:
        P.append(0)

print(max(P))
