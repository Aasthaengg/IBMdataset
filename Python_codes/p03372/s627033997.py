n, c = map(int, input().split())
x = [tuple(map(int, input().split())) for _ in range(n)]

S_cw = [0]
S_ccw = [0]
S_cw_return = [0]
S_ccw_return = [0]

for i in range(n):
    S_cw.append(S_cw[-1]+x[i][1])
    S_ccw.append(S_ccw[-1]+x[n-1-i][1])

for i in range(n):
    S_cw[i+1] -= x[i][0]
    S_ccw[i+1] -= c-x[n-1-i][0]
    S_cw_return.append(S_cw[i+1] - x[i][0])
    S_ccw_return.append(S_ccw[i+1] - (c-x[n-1-i][0]))

S_cw_return_max = [0]
S_ccw_return_max = [0]
for i in range(n):
    if S_cw_return[i+1] > S_cw_return_max[-1]:
        S_cw_return_max.append(S_cw_return[i+1])
    else:
        S_cw_return_max.append(S_cw_return_max[-1])

    if S_ccw_return[i+1] > S_ccw_return_max[-1]:
        S_ccw_return_max.append(S_ccw_return[i+1])
    else:
        S_ccw_return_max.append(S_ccw_return_max[-1])

ans = 0
for i in range(n+1):
    idx = n-i
    ans = max(ans, S_cw[i]+S_ccw_return_max[idx], S_ccw[i]+S_cw_return_max[idx])
print(ans)

