N, Y = map(int, input().split())
Y_dash = Y // 1000
ans = 0
for a in range(0, N+1):
    for b in range(0, N + 1 - a):
        if -9*a - 5*b + 10*N == Y_dash:
            ans = (a, b, N-a-b)
            break
if ans == 0:
    print(-1, -1, -1)
else:
    print(ans[2], ans[1], ans[0])