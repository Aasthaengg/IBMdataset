N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
M = []



for i in range(N):
    TMP = T - (H[i] * 0.006)
    if A >= 0:
        ABS = abs(TMP - A)
    else:
        ABS = abs(A - TMP)
    M.append(ABS)
            
MIN = min(M)
for i in range(len(M)):
    if MIN == M[i]:
        print(i+1)