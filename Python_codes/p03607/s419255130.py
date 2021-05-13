N=int(input())

D={}
for _ in range(N):
    a=int(input())
    try:
        D[a]+=1
    except KeyError:
        D[a]=1

S=0
for b in D:
    S+=D[b]%2
print(S)
