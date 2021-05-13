n = int(input())
t = [list(map(int,input().split())) for _ in range(n)]
t.insert(0,[0,0,0])
for i in range(1,n+1):
    d_sec = t[i][0] - t[i-1][0]
    d_x = abs(t[i][1]- t[i-1][1])
    d_y = abs(t[i][2]- t[i-1][2])
    d_xy = d_x + d_y
    if (d_sec < d_xy) | (d_sec%2 != d_xy%2):
        print("No")
        break
else:
    print("Yes")