N = int(input())
A = list(sorted(list(set(map(int, input().split())))))
while True:
    n = len(A)
    if n == 1 or A[0] == 1:
        break
    B = {A[0]}
    for j in range(1, n):
        m = A[j] % A[0]
        if m != 0:
            B.add(m)
    A = list(sorted(list(B)))
print(A[0])
