N = int(input())
T = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
mod = 10 ** 9 + 7

def solve() :
    if T[-1] != A[0] :
        return 0
        
    for i in range(N) :
        if T[i] == T[-1] :
            break
    for j in range(N - 1, -1, -1) :
        if A[j] == A[0] :
            break
            
    if i > j :
        return 0
        
    ok = [False] * N
    ok[0] = ok[-1] = True
    for i in range(1, N) :
        if T[i] != T[i-1] :
            ok[i] = True
        if A[N-1-i] != A[N-i] :
            ok[N-1-i] = True

    ret = 1
    for i in range(N) :
        if ok[i] : continue
        ret = ret * min(T[i], A[i]) % mod   
    
    return ret
    
print(solve())