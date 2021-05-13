N = int(input())
A = [int(input()) for _ in range(N)]
m = max(A)
if A.count(m) > 1:
    [print(m) for a in A]
else:
    [print(m) if a != m else print(sorted(A)[-2]) for a in A]
