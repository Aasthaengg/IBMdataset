N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
k = 0
s = 0
m = []
l = 0
if sum(B)<=sum(A):
    for i in range(N):
        if A[i] < B[i]:
            k += 1
            s += (B[i]- A[i])
        elif A[i] > B[i]+1:
            m.append(A[i]- B[i])
        elif A[i] == B[i]+1:
            l += (A[i]- B[i])
    if len(m)>1:
        n = sorted(m,reverse = True)
    else:
        n = m
    for j in range(len(m)):
        if s > 0:
            s -= n[j]
            k += 1
        if s <0:
            break
    if (s > 0) and(k > 0):
         k += s
else:
    k = -1
print(k)