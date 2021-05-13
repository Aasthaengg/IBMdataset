A = list(input())
N = len(A)
letter0 = ord('a')
L = [0]*26
for i in range(N):
    L[ord(A[i])-letter0]+=1
out1 = 0
for i in range(26):
    out1 += L[i]*(L[i]-1)//2

out2 = N*(N-1)//2+1
print(out2-out1)