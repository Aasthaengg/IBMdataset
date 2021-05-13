
while True:
    N = int(input())
    if N==0:
        break
    *A, = map(int, input().split())
    V = sum(A)/N
    print((sum((a - V)**2 for a in A)/N)**0.5)
