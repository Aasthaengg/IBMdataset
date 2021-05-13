from math import floor,ceil
K = int(input())
A = [int(x) for x in input().split()]
A.reverse()
jmax, jmin = 2,2

for i in range(0,K):
    mmax,mmin = jmax,jmin
    if mmin % A[i] != 0:
        if (mmin + (A[i] - (mmin % A[i]))) > mmax:
            print(-1)
            exit()

    jmin = ceil(jmin / A[i]) * A[i]
    jmax = floor(jmax / A[i]) * A[i] + A[i] -1

print(jmin, jmax)

#計算量はO(3K)すなわちO(K)