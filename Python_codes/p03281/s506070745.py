N = int(input())
ans = 0

for n in range(1, N+1):
    cnt = 0
    if n%2 == 0:
        continue
    for yaku in range(1, n+1):
        if n%yaku == 0:
            cnt += 1
    if cnt == 8:
        ans += 1
        
print(ans)