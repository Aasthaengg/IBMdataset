import sys
M,K=[int(i) for i in input().split()]
#M,K=1,0
if K>=2**M:
    print(-1)
    sys.exit()
    
if M==1:
    if K==0:
        print(*[0,0,1,1])
        sys.exit()
    else:
        print(-1)
        sys.exit()
L=[]
l=[int(i) for i in range(2**M) if i !=K]
L.extend(l)
L.append(K)
L.extend(l[::-1])
L.append(K)

print(*L)