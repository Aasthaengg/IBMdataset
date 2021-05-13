import collections
n, k, q = map(int, input().split())
A = [int(input()) for _ in range(q)]

C = collections.Counter(A)
for i in range(1, n+1):
    tmp = k - q + C[i]
    if tmp > 0:
        print("Yes")
    else:
        print("No")