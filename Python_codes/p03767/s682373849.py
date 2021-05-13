N=int(input())
A=[int(a) for a in input().split()]
A.sort(reverse=True)
print(sum(A[2*i-1] for i in range(1,N+1)))