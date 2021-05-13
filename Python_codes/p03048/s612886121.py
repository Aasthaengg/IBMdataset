r,g,b,n = map(int,input().split())

ans = 0
for i in range(n+1):
    for j in range(n+1):
        tmp = (r*i)+(g*j)
        if tmp > n:
            break
        else:
            if (n-tmp)%b == 0:
                ans += 1

print(ans)