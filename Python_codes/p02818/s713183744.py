A,B,K=map(int,input().split())
if A >= K:
    A = A-K
else:
    if B>= K-A:
        B = B-(K-A)
    else:
        B = 0
    A = 0
print(A,B)