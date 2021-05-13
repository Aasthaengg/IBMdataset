from functools import reduce
N = int(input())
A = list(map(int, input().split()))
A.sort()
if A[0] == 0:
    print(0)
else:
    p = 1;
    for i in range(N):
        p *= A[i];
        if p > 10**18:
            p = -1;
            break;
    print(p)
