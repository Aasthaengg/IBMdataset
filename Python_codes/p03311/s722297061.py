N=int(input())
A=list(map(int,input().split()))
A=sorted([A[i]-i for i in range(N)])
print(sum([abs(A[i]-A[N//2]) for i in range(N)]))