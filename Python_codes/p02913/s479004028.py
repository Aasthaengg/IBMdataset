#Z[i]:length of the longest list starting from S[i] which is also a prefix of S
#O(|S|)
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

N=int(input())
S=input()
S=[S[i] for i in range(0,N)]

ans=0
for i in range(0,N):
    data=Z_algorithm(S)
    for j in range(0,len(data)):
        ans=max(min(data[j],j),ans)
    S=S[1:]
print(ans)