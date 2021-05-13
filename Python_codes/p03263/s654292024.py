h,w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(h)]

res = []
temp = 0

for i in range(h):
    for j in range(w-1):
        if ab[i][j] % 2 ==0:
            pass
        else:
            ab[i][j] -=1
            ab[i][j+1] += 1
            temp +=1
            res.append(str(i+1)+" "+str(j+1)+" "+str(i+1)+" "+str(j+2))

for k in range(h-1):
    if ab[k][w-1] % 2 ==0:
        pass
    else:
        ab[k][w-1] -=1
        ab[k+1][w-1] +=1
        temp +=1
        res.append(str(k+1)+" "+str(w)+" "+str(k+2)+" "+str(w))
                
print(temp)
for i in range(temp):
    print(res[i])