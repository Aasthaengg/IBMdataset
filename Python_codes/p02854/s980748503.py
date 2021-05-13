N = int(input())
A = list(map(int, input().split()))

length = sum(A)
center = length / 2

now = 0
for i in range(N):
    now += A[i]
    if now == center:
        print(0)
        break
    if now > center:
        print(int(min(now-center, center-now+A[i]) * 2))
        break