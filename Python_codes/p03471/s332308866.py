n,y = map(int, input().split())
ans = -1, -1, -1
for i in range(n+1):
    for j in range(n-i+1):
        if i*10000+j*5000+(n-i-j)*1000==y:
            ans = i, j, (n-i-j)
            break
    else:
        continue
    break
print(*ans)
