N = int(input())
txy = list(list(map(int, input().split())) for _ in range(N))
dt = 0
dx = 0
dy = 0
for i in range(N):
    if abs(txy[i][1]-dx)+abs(txy[i][2]-dy) > txy[i][0]-dt or (txy[i][1]+txy[i][2])%2 != txy[i][0]%2:
        print("No")
        break
    dt = txy[i][0]
    dx = txy[i][1]
    dy = txy[i][2]
else:
    print("Yes")