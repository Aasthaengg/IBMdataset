n = int(input())

cnt = [[0]*10 for _ in range(10)]

for i in range(1,n+1):
    check = str(i)
    head = int(check[0])
    tail = int(check[-1])
    cnt[head][tail] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += cnt[i][j]*cnt[j][i]
        
print(ans)