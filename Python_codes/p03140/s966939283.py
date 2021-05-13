import collections

N = int(input())
A = input()
B = input()
C = input()

ans = 0
for i in range(N):
    l = []
    l.append(A[i])
    l.append(B[i])
    l.append(C[i])
    c = collections.Counter(l)
    c_len = len(c)
    if c_len == 2:
        ans += 1
    elif c_len == 3:
        ans += 2

print(ans)
