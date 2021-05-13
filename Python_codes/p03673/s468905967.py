n = int(input())
A = list(input().split())
if n % 2:
    print(" ".join(A[::2][::-1]), " ".join(A[1::2]))
else:
    print(" ".join(A[1::2][::-1]), " ".join(A[::2]))
