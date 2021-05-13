from itertools import accumulate
n,k = map(int,input().split())
A = list(map(int,input().split()))
for _ in range(k):
    c = [0]*n
    for i,j in enumerate(A):
        l = max(0,i-j)
        r = min(n-1,i+j)
        c[l] += 1
        if r+1 < n:
            c[r+1] -= 1
    #print(c)
    d = list(accumulate(c))
    if A == d:
        break
    A = d
print(" ".join(map(str,A)))