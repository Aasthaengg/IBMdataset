N = int(input())
t = [list(map(int, input().split())) for _ in range(N)]
t.insert(0, [0, 0, 0])
x = [t[i][1] for i in range(N+1)]
y = [t[i][2] for i in range(N+1)]
t = [t[i][0] for i in range(N+1)]
for i in range(1, N+1):
    if abs(x[i] - x[i-1]) + abs(y[i] - y[i-1]) > t[i] - t[i-1] or (abs(x[i] - x[i-1]) + abs(y[i] - y[i-1])) %2 != (t[i] - t[i-1]) % 2:
        print('No')
        exit()
print('Yes')
