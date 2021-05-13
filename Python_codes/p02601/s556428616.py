def find(A,B,C,K):
#     A<B<C
    for i in range(K+1):
        v1 = i
        v2 = K - i
        B0 = B*(2**v1)
        C0 = C*(2**v2)
        if A < B0 and B0 < C0:
            return True
    return False

A,B,C = list(map(int,input().strip().split()))
K = int(input())
if find(A,B,C,K):
    print("Yes")
else:
    print("No")