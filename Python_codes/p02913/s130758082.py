N=int(input())
S=input()
ans=0

def Z_algorithm(s):
    N = len(s)
    Z_alg = [0]*N

    Z_alg[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and s[j] == s[i+j]:
            j += 1
        Z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_alg[k]<j:
            Z_alg[i+k] = Z_alg[k]
            k += 1
        i += k
        j -= k
    return Z_alg

ans=0  
for i in range(N):
  d=S[i:]
  D=Z_algorithm(d)
  for j in range(N-i):
    ans=max(ans,min(j,D[j]))
print(ans)