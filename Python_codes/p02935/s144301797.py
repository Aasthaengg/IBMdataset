N=int(input())
*V,=map(int,input().split())

V.sort()
ans=(V[0]+V[1])/2
i=2
while i<N:
    ans=(ans+V[i])/2
    i+=1

print(ans)