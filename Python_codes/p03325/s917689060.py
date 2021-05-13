def Div2Count(N):
    Count = 0
    while N%2==0:
        N = N//2
        Count += 1
    return Count
  
N = int(input())
A = [Div2Count(int(X)) for X in input().split()]
print(sum(A))