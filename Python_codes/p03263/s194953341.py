h,w = map(int,input().split())
coins = []
ans = []
for i in range(h):
    coins.append(list(map(int,input().split())))
for i in range(h-1):
    for j in range(w):
        if coins[i][j] % 2 != 0:
            coins[i][j] -= 1
            coins[i+1][j] += 1
            ans.append((i+1,j+1,i+2,j+1))
for i in range(w-1):
    if coins[h-1][i] % 2 != 0:
        coins[h-1][i] -= 1
        coins[h-1][i+1] += 1
        ans.append((h,i+1,h,i+2))
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])

