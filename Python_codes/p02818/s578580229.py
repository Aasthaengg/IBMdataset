A, B, K = map(int, input().split())

if A>=K:
    A = A - K
    print(A,B)
    exit()
else :
    K = K - A
    A = 0

if B>=K:
    B = B-K
else :
    B = 0

print(A,B)