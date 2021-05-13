N, H = list(map(int, input().split()))
A = [0]*N
B = [0]*N
for i in range(N):
    a, b = list(map(int, input().split()))
    A[i], B[i] = a, b
a = max(A)
T = 0
ct = 0
B = reversed(sorted(B))
for b in B:
    if b > a:
        ct += 1
        T += b
    if T >= H:
        break
print(ct + max((H-T+a-1)//a, 0))
