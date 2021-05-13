N = int(input())
P = [int(input()) for _ in range(N)]

Q = [-1]*N
for i in range(N):
    Q[P[i]-1] = i

x = 1
tmp = 1
for i in range(1,N):
    if Q[i] > Q[i-1]:
        tmp += 1
        x = max(x, tmp)
    else:
        tmp = 1

print(N-x)