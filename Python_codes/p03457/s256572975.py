n = int(input())
t_l = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
t_t = [[abs(t_l[i][0]-t_l[i-1][0]), abs(t_l[i][1]-t_l[i-1][1]), abs(t_l[i][2]-t_l[i-1][2])] for i in range(1,n+1)]
ans = "Yes"

for j in t_t:
    t, x, y = j
    if t < x + y:
        ans = "No"
        break
    elif t % 2 != (x + y) % 2:
        ans = "No"
        break
print(ans)
