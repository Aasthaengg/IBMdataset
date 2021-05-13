n = int(input())
l = [[0, 0, 0]] + list(list(map(int, input().split())) for i in range(n))

for i in range(1, n+1):
    dt = l[i][0] - l[i-1][0]
    dx = abs(l[i][1] - l[i-1][1])
    dy = abs(l[i][2] - l[i-1][2])
    
    tmp = dt - dx - dy
    if tmp < 0 or tmp % 2 == 1:
        print('No')
        break
else:
    print('Yes')
