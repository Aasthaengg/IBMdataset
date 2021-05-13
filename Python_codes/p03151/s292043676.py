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
    D = sorted([i for i in C if i > 0], reverse=True)
    r = [D[0]]
    for i in range(len(D)-1):
        r.append(r[i] + D[i+1])
    print(len([i for i in C if i < 0])+bisect.bisect_left(r, sum(-i for i in C if i < 0))+1)
