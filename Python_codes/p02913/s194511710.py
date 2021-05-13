def Z_Algorithm(S):
    N = len(S)
    Z = [0]*N
    Z[0] = N
    
    i = 1   #左
    j = 0   #差分

    while i < N:
        while i + j < N and S[j] == S[j + i]:
            j += 1
        Z[i] = j

        if j == 0:
            i += 1
            continue

        k = 1   # 差分
        while k < j and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        
        i += k
        j -= k
    
    return Z

def calc(S):
    N = len(S)
    Z = Z_Algorithm(S)

    res = 0
    for i in range(N):
        res = max(res, min(Z[i], i))
    
    return res

N = int(input())
S = input()

res = 0

for i in range(N):
    res = max(res, calc(S[i:]))

print(res)