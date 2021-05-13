n = int(input())
d, x = map(int, input().split())

ans = x
for _ in range(n):
    a = int(input())
    cnt = 1
    
    tmp = a + 1
    if tmp <= d: cnt += 1
      
    while True:
        tmp += a
        if tmp <= d: cnt += 1
        else: break
        
    ans += cnt

print(ans)