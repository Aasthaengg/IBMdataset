def Divide2Count(N):
    Count = 0
    while True:
        if N%2==0:
            Count += 1
            N //= 2
        else:
            break
    return Count

N = int(input())
A = [Divide2Count(int(X)) for X in input().split()]
print(min(A))