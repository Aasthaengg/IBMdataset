A, B, C, K = list(map(int, input().split()))

if A+B>=K:
    print(min(A, K))
else:
    print(A-(K-A-B))
