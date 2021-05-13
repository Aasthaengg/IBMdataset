A, B, K = map(int, input().split())

if A+K-1 < B-K+1:
    l = list(range(A, A+K))+list(range(B-K+1, B+1))
else:
    l = list(range(A, B+1))

for v in l:
    print(v)