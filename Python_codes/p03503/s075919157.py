n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = -10 ** 20
for i in range(1, 2 ** 10):
    cnt = [0] * n
    calc = 0
    for j in range(10):
        if i >> j & 1:
            for k in range(n):
                if f[k][j] == 1:
                    cnt[k] += 1
                
    for k in range(n):
        calc += p[k][cnt[k]] 
    
    ans = max(ans, calc)

print(ans)
            
