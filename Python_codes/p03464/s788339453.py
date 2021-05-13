N = int(input())
A = list(map(int,input().split()))
A.append(2)
mi = 2
mx = 2
for i in range(N-1,-1,-1):
    # A[i]人に分けた結果 mi ~ mx人が残った
    mi = (mi + A[i] - 1) // A[i] * A[i]
    mx = mx // A[i] * A[i]
    if mi > mx:
        print(-1)
        exit(0)
    mx += A[i] - 1
print(mi,mx)
