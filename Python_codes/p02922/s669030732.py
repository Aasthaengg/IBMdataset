a, b = map(int, input().split())

cnt = 1
ans = 0

while cnt < b:
    if cnt >= b:
        break
    else:
        cnt -= 1
    cnt += a
    ans += 1
    
print(ans)