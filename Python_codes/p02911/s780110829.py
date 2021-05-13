n, k, q = map(int, input().split())
A = [int(input()) for i in range(q)]
C = [0 for i in range(n)]
for i in range(q):
    C[A[i]-1] += 1
for i in range(n):
    c = C[i]
    if k - q + c <= 0:
        print ("No")
    else:
        print ("Yes")