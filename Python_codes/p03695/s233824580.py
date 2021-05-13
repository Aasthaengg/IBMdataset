n = int(input())
rate = list(map(int,input().split()))
ratecolor = 0
free = 0
ratecolor = 0
color = [0]*9
for i in range(n):
    if(rate[i] >= 3200):
        free += 1
    else:
        for j in range(9):
            if(rate[i] < j*400 + 400):
                if(color[j] == 0):
                    color[j] += 1
                    ratecolor += 1
                break
print(ratecolor if ratecolor != 0 else 1,ratecolor+free)

