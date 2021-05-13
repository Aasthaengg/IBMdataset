N, K = map(int, input().split())
A = [int(i) for i in input().split()]
A.sort()

a = []
a.append(A[0])
c = []
c.append(1)
for i in range(N-1):
    if A[i] == A[i+1]:
        c[-1] += 1
    else:
        a.append(A[i+1])
        c.append(1)

ans = 0
if len(a) <= K:
    ans = 0
else:
    c.sort()
    for i in range(len(a)-K):
        ans += c[i]

print(ans)
