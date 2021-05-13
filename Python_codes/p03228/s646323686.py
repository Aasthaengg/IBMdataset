A, B, K = map(int, input().split())

while K > 0:
    if A % 2 == 1:
        A -= 1
    B = B + (A//2)
    A = A // 2
    K -= 1
    if K < 1:
        break
    if B % 2 == 1:
        B -= 1
    A = A + (B//2)
    B = B // 2
    K -= 1

print("{0} {1}".format(A, B))
