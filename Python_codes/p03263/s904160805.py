h,w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
answer = []
count = 0
for i in range (0,h-1):
    for j in range (0,w):
        if (a[i][j] % 2 != 0):
            a[i+1][j] += 1
            count += 1
            answer.append([i+1,j+1,i+2,j+1]) #座標に調整(両座標+1)
for k in range (0,w-1):
    if (a[h-1][k] % 2 != 0):
        a[h-1][k+1] += 1
        count += 1
        answer.append([h,k+1,h,k+2]) #同
print(count)
for l in range (0,len(answer)):
    print(*answer[l])