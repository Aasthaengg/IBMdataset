N, M = map(int, input().split())
if N%2 != 0:
    first = 1
    for i in range(M):
        print(first, N-i)
        first += 1
else:
    mid = N//2
    for i in range((M+1)//2):
        print(i+1,mid-i)
    for i in range(M//2):
        print(mid+1+i, N-1-i)
