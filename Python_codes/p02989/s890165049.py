N=int(input())
A=list(map(int,input().split()))
A.sort()
c=N//2-1
print(A[c+1]-A[c])
