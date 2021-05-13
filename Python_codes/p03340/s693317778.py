N = int(input())

A = list(map(int,input().split()))

S = A[0]
X = A[0]
l = 0
r = 0
count = 0

while r < N and l <= r:
    if S == X and r < N-1:
        r += 1
        S += A[r]
        X = X ^ A[r]
    elif S == X and r == N-1:
        count += r-l+1
        l += 1
        S -= A[l-1]
        X = X ^ A[l-1]
    else:
        count += r-l
        l += 1
        S -= A[l-1]
        X = X ^ A[l-1]
    #print([l,r,count])

print(count)