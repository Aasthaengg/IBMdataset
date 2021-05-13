
[N,A,B] = list(map(int,input().split()))
out=0

for dam in range(1,N+1):
    L = list(str(dam))
    wa=0
    for i in range(len(L)):
        wa+=int(L[i])
    if wa>=A and wa<=B:
        out+=int(''.join(L))
    # print('L,wa,out:',L,wa,out)

print(out)