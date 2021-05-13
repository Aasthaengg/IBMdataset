# Tsundoku
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
if M > N:
    N,M = M,N
    A,B = B,A
a = [0]
b = [0]
for _ in range(max(N, M)):
    if _ < min(N,M):
        a.append(a[_] + A[_])
        b.append(b[_] + B[_])
    else:
        a.append(a[_] + A[_])
ans = 0
j = M
for i in range(N+1):
    if a[i] > K:
        break
    while b[j] > K - a[i]:
        j -= 1
    ans = max(ans, i+j)
print(ans)