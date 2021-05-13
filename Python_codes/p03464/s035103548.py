import sys
 
K = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
 
if A[-1] != 2:
    print(-1)
    sys.exit()
 
l = 2
r = 2
for i in range(K-2, -1, -1):
    l = ((l - 1) // A[i] + 1) * A[i]
    r = ((r + A[i+1] - 1) // A[i]) * A[i] 
 
    if r < l:
        print(-1)
        sys.exit()
 
print(l, r + A[0] - 1)