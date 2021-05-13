N = int(input())
A = list(map(int, input().split()))
minA = min(A)
for i in range(N):
    A[i] -= i+1 
minA = min(A)
for i in range(N):
    A[i] -= minA
A.sort()
#print(A)

if N %2 == 1:
    ans = A[(N-1)//2]
    t = 0
    for i in range(N):
        t += abs(A[i]-ans)
    ans = t

else:
    ans1 = A[(N)//2]
    ans2 = A[(N)//2 -1]
    t = 0
    for i in range(N):
        t += abs(A[i]-ans1)
    s = 0
    for i in range(N):
        s += abs(A[i]-ans2)
    ans = min(t, s)

print(ans)

