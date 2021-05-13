n = int(input())
A = tuple(map(int, input().split()))
C = [0] * n
for a in A:
    C[a-1] += 1
for c in C:
    print(c)
