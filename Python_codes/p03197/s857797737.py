N = int(input())
A = [int(input()) % 2 == 0 for _ in range(N)]

if all(A):
    print("second")
else:
    print("first")
