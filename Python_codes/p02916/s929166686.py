N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
print(sum(B)+sum(C[A[n]-1] for n in range(N-1) if A[n]+1==A[n+1]))