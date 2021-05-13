n,y = map(int,input().split())
ans = [-1,-1,-1]
if 10000 * n >= y:
    for i in range((y//10000)+1):
        for j in range(n-i+1):
                if 10000 * i + 5000 * j + 1000 * (n-i-j) == y:
                    ans = [i,j,n-i-j]
print(*ans)