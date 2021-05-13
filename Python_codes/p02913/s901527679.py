N = int(input())
S = input()

def z_algorithm(s):
    n = len(s)
    res = [0] * n
    i = 1
    j = 0
    while i < n:
        while i + j < n and s[j] == s[i + j]:
            j += 1
        res[i] = j
        
        if j == 0:
            i += 1
            continue
            
        k = 1
        while i + k < n and k + res[k] < j:
            res[i + k] = res[k]
            k += 1
            
        i += k
        j -= k
        
    return res

ans = 0
for i in range(N):
    lcp = z_algorithm(S[i:])
    tmp = max(min(lcp[j], j) for j in range(N - i))
    ans = max(ans, tmp)
print(ans)
