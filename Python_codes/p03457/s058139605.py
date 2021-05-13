n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
now = 0
now_t = 0
flag = 1
for i in range(n):
    t,x,y = s[i][0],s[i][1],s[i][2]
    next = x+y
    dist = abs(next - now)
    time = t - now_t
    if dist == 0 and time == 1:
        print('No')
        exit()
    if dist > time:
        print('No')
        exit()
    elif dist == time:
        now_t = t
        now = next
    else:
        if abs(dist - time) % 2 == 0:
            now_t = t
            now = next
        else:
            print('No')
            exit()
print('Yes')