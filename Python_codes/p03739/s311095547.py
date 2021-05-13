N = int(input())
A = list(map(int,input().split()))
mans = 0
msum = 0
for i in range(N):
    if i%2:
        if msum + A[i] <= 0:
            mans += abs(msum + A[i])+1
            msum = 1
        else:
            msum += A[i]
    else:
        if msum + A[i] >= 0:
            mans += msum + A[i]+1
            msum = -1
        else:
            msum += A[i]
pans = 0
psum = 0
for i in range(N):
    if i%2:
        if psum + A[i] >= 0:
            pans += psum + A[i]+1
            psum = -1
        else:
            psum += A[i]
    else:
        if psum + A[i] <= 0:
            pans += abs(psum + A[i])+1
            psum = 1
        else:
            psum += A[i]

print(min(pans,mans))