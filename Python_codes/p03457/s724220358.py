import sys
n = int(input())
data = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    if i>0:
        distance = abs(data[i][1]-data[i-1][1])+abs(data[i][2]-data[i-1][2])
        time = abs(data[i][0]-data[i-1][0])
    else:
        distance = abs(data[i][1])+abs(data[i][2])
        time = abs(data[i][0])
    
    if distance <= time:
        if (data[i][0] + data[i][1] + data[i][2])% 2 == 0:
            continue
        else:
            break
    else:
        break
else:
    print("Yes")
    sys.exit()

print("No")
