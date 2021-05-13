import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted([A[i] - B[i] for i in range(N)])
if sum(C) < 0:
    print(-1)
elif min(C) >= 0:
    print(0)
else:
    D = [i for i in C if i < 0]
    m = sum(D)
    for i in range(N-1,-1,-1):
        m += C[i]
        if m >= 0:
            print(len(D)-i+N)
            break
