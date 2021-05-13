N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

u_cnt = [0] * N
d_cnt = [0] * N

t = 0
for i in range(N):
    while t < N and A[t] < B[i]:
        t += 1
    u_cnt[i] = t

t = N-1
for i in range(N-1,-1,-1):
    while t >= 0 and C[t] > B[i]:
        t -= 1
    d_cnt[i] = N - 1 - t

ans = 0
for i in range(N):
    ans += u_cnt[i] * d_cnt[i]

print(ans)