R,G,B,N = map(int, input().split())

count = 0

for r in range(3001):
    for g in range(3001):
        redball = r*R
        greenball = g*G
        tempbull = N - (redball + greenball)
        
        if (redball >= 0) and (greenball >= 0) and (tempbull >= 0):
            if (redball + greenball + tempbull == N) and (tempbull % B == 0):
                count = count + 1

print(count)