N = int(input())
H = [int(x) for x in input().split()]
Count = 0
MAXC  = 0
for T in range(0,N-1):
    if H[T]>=H[T+1]:
        Count += 1
    else:
        Count = 0
    if Count > MAXC:
        MAXC = Count
print(MAXC)