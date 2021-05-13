N = int(input())
A = [int(input()) for _ in range(N)]

if all(v % 2 == 0 for v in A):
    print("second")
else:
    print("first")
