N, T = map(int, input().split())
t = list(map(int, input().split()))

x = 0
for i in range(N):
    if i < N-1:
        x += min(T, t[i+1]-t[i])
    else:
        x += T

print(x)