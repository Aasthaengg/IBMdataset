import math
K = int(input())
A = list(map(int,input().split()))
M,m = 2,2
A = reversed(A)
for i in A:
    M = (M//i)*i+(i-1)
    m = math.ceil(m/i)*i
    if m > M:
        print(-1)
        exit()
print(m,M)