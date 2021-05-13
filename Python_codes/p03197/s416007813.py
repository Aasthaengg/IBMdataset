N = int(input())
A = [int(input())%2 for _ in range(N)]
if 1 in A:
    print("first")
else:
    print("second")