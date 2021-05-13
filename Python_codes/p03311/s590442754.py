import math
N = int(input())
A = sorted([int(v)-i for i, v in enumerate(input().split(), start=1)])

if N % 2 == 1:
    ans = sum([abs(a-A[N//2]) for a in A])
else:
    b0 = (A[N//2-1]+A[N//2])//2
    b1 = math.ceil(A[N//2-1]+A[N//2])
    ans = min(sum([abs(a-b0) for a in A]), sum([abs(a-b1) for a in A]))

print(ans)
