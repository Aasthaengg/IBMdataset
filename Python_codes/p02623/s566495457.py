#template
def inputlist(): return [int(j) for j in input().split()]
#template
N,M,K = inputlist()
A = inputlist()
B = inputlist()
a = [0]*(N+1)
b = [0]*(M+1)
for i in range(N):
    a[i+1] = a[i] + A[i]
for i in range(M):
    b[i+1] = b[i] + B[i]
ans,j = 0,M
for i in range(N+1):
    if a[i] > K:
        break
    while b[j] > K-a[i]:
        j -=1
    ans = max(ans,i+j)
print(ans)