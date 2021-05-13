N, A, B = map(int, input().split())
if A > B or (N == 1 and A < B):
    print(0)
    exit()
if N == 1 and A == B:
    print(1)
    exit()
mx = A+B+B*(N-2)
mn = A+B+A*(N-2)
print(mx-mn+1)
