N = int(input())

prev_t = 0
prev_x = 0
prev_y = 0

for i in range(N):
    t,x,y = map(int,input().split())
    dist = abs(x-prev_x)+ abs(y-prev_y)
    if dist > (t-prev_t) or (dist+(t - prev_t))%2:
        print("No")
        exit()
    prev_t = t
    prev_x = x
    prev_y = y

print("Yes")
