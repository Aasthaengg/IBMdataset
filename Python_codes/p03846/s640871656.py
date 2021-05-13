def check():
    if N %2 == 1:
        if A.pop(0) != 0:
            return 0
        pair = 2
    else:
        pair = 1
    
    for i in range(N//2):
        if A[2*i] == pair and A[2*i+1] == pair:
            pair += 2
        else:
            return 0
    return 1

N = int(input())
A = list(map(int, input().split()))
A.sort()
mod = int(1e9 +7)
if check() == 0:
    print(0)
else:
    print(pow(2, N//2, mod))