N,K = map(int,input().split())
*A, = map(int,input().split())

for a,b in zip(A,A[K:]):
    print("Yes" if b>a else "No")