N = int(input())
A = list(map(int, input().split()))

L = [ i+1+A[i] for i in range(N) ]
R = [j+1-A[j] for j in range(N) ]

Ld = {}
Rd = {}

for i in range(N):
    if R[i] in Rd.keys():
        Rd[R[i]] += 1
    else:
        Rd[R[i]] = 1

ans = 0
for i in range(N):
    if L[i] in Rd.keys():
        ans += Rd[L[i]]
    if L[i] == R[i]:
        ans -= 1
        
print(ans)