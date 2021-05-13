def Dev2Count(N):
    Count = 0
    while True:
        if N%2==0:
            Count += 1
            N //= 2
        else:
            break
    return Count
  
N = int(input())
print(2**max(Dev2Count(T) for T in range(1,N+1)))