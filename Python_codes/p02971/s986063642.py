n = int(input())
A = [int(input()) for _ in range(n)]
S = sorted(A)

for a in A:
    print(S[-1] if a != S[-1] else S[-2])