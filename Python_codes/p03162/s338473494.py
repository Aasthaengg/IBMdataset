N = int(input())
a, b, c = [0], [0], [0]
for i in range(N):
    a_i, b_i, c_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)
    c.append(c_i)
DP = [[0 for j in range(3)] for i in range(N+1)]
for days in range(1, N+1):
    for ABC in range(3):
        if ABC == 0:
            DP[days][ABC] = max(DP[days-1][1], DP[days-1][2]) + a[days]
        elif ABC == 1:
            DP[days][ABC] = max(DP[days-1][0], DP[days-1][2]) + b[days]
        elif ABC == 2:
            DP[days][ABC] = max(DP[days-1][0], DP[days-1][1]) + c[days]
print(max(DP[N]))

