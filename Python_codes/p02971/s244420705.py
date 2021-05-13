n = int(input())
A = [int(input()) for _ in range(n)]
SA = sorted(A, reverse=True)
ma = max(A)
for a in A:
    if a == ma:
        print(SA[1])
    else:
        print(ma)
