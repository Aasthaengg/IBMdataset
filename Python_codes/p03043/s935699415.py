n,k = map(int, input().split())

ans = 0
for i in range(1,n+1):
    num = i
    cnt = 0
    while True:
        if num >= k: break
        num *= 2
        cnt += 1
    prob = 1/pow(2,cnt)
    ans += prob

ans /= n
print(ans)