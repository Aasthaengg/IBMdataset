n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n-1, -1, -1):
    a = li[i][0]
    b = li[i][1]
    
    a += ans
    
    if a%b == 0:
        continue
    s = b - a%b
    ans += s
    
print(ans)