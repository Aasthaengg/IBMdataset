n,K = map(int,input().split())
xy = [[int(i) for i in input().split()] for j in range(n)]

ans = 10**20

for i in range(n):
    for j in range(i+1,n):
        if K == 2:
            ans = min(ans,abs(xy[i][0]-xy[j][0])*abs(xy[i][1]-xy[j][1]))
        for k in range(j+1,n):
            if K == 2:
                break
            max_x_old = max(xy[i][0],xy[j][0],xy[k][0])
            min_x_old = min(xy[i][0],xy[j][0],xy[k][0])
            max_y_old = max(xy[i][1],xy[j][1],xy[k][1])
            min_y_old = min(xy[i][1],xy[j][1],xy[k][1])
            if K == 3:
                #max_x = max(xy[i][0],xy[j][0],xy[k][0])
                #min_x = min(xy[i][0],xy[j][0],xy[k][0])
                #max_y = max(xy[i][1],xy[j][1],xy[k][1])
                #min_y = min(xy[i][1],xy[j][1],xy[k][1])
                ans = min(ans,abs(max_x_old-min_x_old)*abs(max_y_old-min_y_old))
            for l in range(k+1,n):
                if K == 2 or K == 3:
                    break
                cnt = 0
                max_x = max(max_x_old,xy[l][0])
                min_x = min(min_x_old,xy[l][0])
                max_y = max(max_y_old,xy[l][1])
                min_y = min(min_y_old,xy[l][1])
                for m in range(n):
                    if xy[m][0] >= min_x and xy[m][0] <= max_x\
                       and xy[m][1] >= min_y and xy[m][1] <= max_y:
                           cnt += 1
                if cnt >= K:
                    #print(cnt,K)
                    ans = min(ans,(max_x-min_x)*(max_y-min_y))
                
print(ans)