N=int(input())

M=10**9
for i in range(1,N//2+1):
    a=list(str(i))
    b=list(str(N-i))
    #print(a,b)
    k=0
    for q in range(len(a)):
        k+=int(a[q])
    for p in range(len(b)):
        k+=int(b[p])
    M=min(M,k)
print(M)