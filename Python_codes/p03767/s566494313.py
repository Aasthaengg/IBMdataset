N=int(input())
A=sorted(list(map(int,input().split(' '))),reverse=True)
print(sum(A[1:2*N:2]))