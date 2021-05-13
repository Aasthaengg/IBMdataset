N = int(input())
A = sorted(list(map(int,input().split())))
n = A[-1]
k = A[0]
for i in range(1,N-1):
    j = A[i]
    if k<=n//2 and j<=n//2:
        k = max(k,j)
    elif k<=n//2 and j>n//2:
        if k<n-j:
            k = j
    elif k>n//2 and j<=n//2:
        if n-k<j:
            k = j
    elif k>n//2 and j>n//2:
        if n-k<n-j:
            k = j
print(n,k)