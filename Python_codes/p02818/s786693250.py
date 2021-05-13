A, B, K = map(int, input().split())
print(0, 0) if B-K+A<0 else print(A-K, B) if A>=K else print(0, B-K+A)