from collections import Counter

N, P = map(int, input().split())
A = list(map(int, input().split()))
n0 = 0
n1 = 0
for i, a in enumerate(A):
    b = a % 2
    A[i] = b
    if b == 0:
        n0 += 1
    else:
        n1 += 1
C1 = [1]
for i in range(n1):
    C1.append(C1[-1] * (n1-i)//(i+1))


ans = 0
for i in range(0, 51, 2):
    if i + P > n1:
        break
    ans += C1[i+P] * (2**(n0))


print(ans)

