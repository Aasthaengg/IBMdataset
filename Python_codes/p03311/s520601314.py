N = int(input())
A = list(map(int, input().split()))
A = sorted([A[i] - (i+1) for i in range(N)])

if N % 2 == 1:
    median = A[N//2]
    sad = sum([abs(A[i] - median) for i in range(N)])
else:
    hoge, fuga = (A[N//2-1]+A[N//2])//2, (A[N//2-1]+A[N//2])//2+1
    sad = min(sum([abs(A[i] - hoge) for i in range(N)]), sum([abs(A[i] - fuga) for i in range(N)]))
print(sad)