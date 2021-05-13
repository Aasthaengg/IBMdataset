s = str(input())

n = len(s)

L = [0]*(n+1)
cnt = 0
for i in range(n):
    if s[i] == '<':
        cnt += 1
    else:
        cnt = 0
    L[i+1] = cnt


R = [0]*(n+1)
cnt = 0
for i in reversed(range(n)):
    if s[i] == '>':
        cnt += 1
    else:
        cnt = 0
    R[i] = cnt

A = [0]*(n+1)
for i in range(n+1):
    A[i] = max(L[i], R[i])
print(sum(A))
