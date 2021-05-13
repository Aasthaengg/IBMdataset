N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
 
if sum(A) < sum(B):
    print(-1)
    exit(0)
 
t = 0
m = 0
L = []
for k in range(N):
    if A[k] > B[k]:
        L.append(A[k]-B[k])
    else:
        m += B[k] - A[k]
        t += 1
 
if m == 0:
    print(0)
    exit(0)
 
L = (sorted(L))[::-1]
for e in L:
    m -= e
    t += 1
    if m <= 0:
        break
print(t)