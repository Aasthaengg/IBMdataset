D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]

L = [0]*26

v = 0
for i in range(1, D+1):
    t = int(input())
    t -= 1
    v += S[i-1][t]
    L[t] = i
    for j in range(26):
        v -= C[j]*(i-L[j])
    print(v)
