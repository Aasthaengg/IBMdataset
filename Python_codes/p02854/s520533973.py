N = int(input())
A = list(map(int, input().split()))
sm = sum(A)
t = 0
for i in range(N):
    if t > sm/2:
        break
    else:
        t += A[i]
        s = t-A[i]
u = 2*t - sm
v = sm - 2*s
print(min(u,v))