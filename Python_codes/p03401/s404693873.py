def resolve():
    N=int(input())
    A=list(map(int,input().split()))
    A=[0]+A+[0]
    total=sum([abs(A[i+1]-A[i]) for i in range(N+ 1)])

    for i in range(N):
        print(total-(abs(A[i+1]-A[i])+abs(A[i+2]-A[i+1]))+abs(A[i+2]-A[i]))



resolve()