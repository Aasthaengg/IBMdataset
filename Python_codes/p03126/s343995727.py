N,M=map(int,input().split())
A=list(map(int,input().split()))
A.pop(0)

if N>1:
    for _ in range(N-1):
        B=list(map(int,input().split()))
        B.pop(0)
        A=[num for num in A if num in B]

print(len(A))