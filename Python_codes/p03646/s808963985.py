N=int(input())

if N<=50:
    A=[0 for i in range(50)]
    for i in range(N):
        A[i]=50
    print(50)
    print(*A)
else:
    A=[50-i for i in range(50)]
    N-=50
    for i in range(50):
        A[i]+=N//50
    for i in range(N%50):
        A[i]+=1
    print(50)
    print(*A)