from collections import defaultdict
def query(result, p, b, c):
    result += (c-b) * p[b]
    p[c] += p[b]
    p[b] = 0
    return result, p
N = int(input())
A = [int(i) for i in input().split()]
p = defaultdict(int)
for i in range(N):
    p[A[i]]+= 1
result = sum(A)
Q = int(input())
for i in range(Q):
    b, c = [int(i) for i in input().split()]
    result, p = query(result, p, b, c)
    print(result)