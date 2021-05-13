import math

A,B = map(int,input().split())

ans = 0

for i in range(1005):
    if math.floor((i*8)/100) == A and math.floor((i*1)/10) == B:
        ans = i
        print(ans)
        break

if ans == 0:
    print(-1)