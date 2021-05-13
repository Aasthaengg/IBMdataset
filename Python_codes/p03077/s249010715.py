N = int(input())
A = [int(input()) for i in range(5)]
m = min(A)
cnt = (N - 1) // m + 1
print(cnt + 4)