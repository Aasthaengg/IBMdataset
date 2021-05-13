N = int(input())

A = list(map(int,input().split()))

A.sort()

npl = A[-1]
nmi = A[0]

del A[0]
del A[-1]
lis = []

for i in A:

    if i < 0:
        lis.append([npl,i])
        npl -= i

    else:
        lis.append([nmi,i])
        nmi -= i

lis.append([npl,nmi])
print (npl-nmi)

for i in lis:

    print (i[0],i[1])
