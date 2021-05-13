k, s = map(int,input().split())

ans = 0
for x in range(0,k+1):
    for y in range(0,s-x+1):
        if y > k:
            break
        z = s-x-y
        if 0<=z<=k:
            ans += 1
print(ans)