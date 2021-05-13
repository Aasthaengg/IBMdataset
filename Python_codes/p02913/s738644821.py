from collections import deque

def Z_alg(S):
    
    length = len(S)
    Z = [0] * (length + 1)
    Z[0] = length
    i, j = 1, 0
    ret = 0

    while i < length:
        while i + j < length and S[j] == S[i + j]:  j += 1
        Z[i] = j
        if i - Z[i] >= 0:  ret = max(ret, Z[i])
        if(j == 0):
            i += 1
            continue
        k = 1
        while k < j and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
            if (i + k) - Z[i + k] >= 0:  ret = max(ret, Z[i + k])
        i += k
        j -= k
        
    return ret

N = int(input())
S = input()
ans = 0
s = deque(S)
while s:
    ans = max(ans, Z_alg(s))
    s.popleft()  
print(ans)