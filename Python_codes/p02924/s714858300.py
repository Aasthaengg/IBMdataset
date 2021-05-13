N = int(input())
if N % 2 == 1:
    print(N * (N//2))
else:
    print(N * (N//2-1) + (N//2))