N = int(input())
S = input().rstrip()
A, B, c1, c2 = [], [], 0, 0
for s in S:
    if s=="W": c1 += 1
    A.append(c1)
for s in reversed(S):
    if s=="E": c2 += 1
    B.append(c2)
B.reverse()
res = float("inf")
A += [0]
B += [0]
for i in range(N):
    res = min(A[i-1] + B[i+1], res)
print(res)