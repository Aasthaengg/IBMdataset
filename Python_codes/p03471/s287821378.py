N, Y =map(int, input().split())
c = 0
for n in range(N+1):
    if c == 1:
        break
    for m in range(N-n+1):
            l = N -n - m
            if Y ==( n*10000 + m *5000 + l *1000) and (n + m + l) == N:
                print(n , m , l)
                c = 1
                break
if c != 1:
    print(-1 , -1 , -1)