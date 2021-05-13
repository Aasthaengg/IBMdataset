N=int(input())
S=0
i=0
while S<N:
    i+=1
    S+=i

T=set()
for a in range(i,0,-1):
    if N>=a:
        T.add(a)
        N-=a

print("\n".join(map(str,T)))
