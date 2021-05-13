n,k = map(int,input().split())
coin = 1/2
pred = 1/n
ans = 0
for i in range(1, n+1):
    point = i
    count = 0
    while k > point:
        point *= 2
        count += 1
    ans += pred * coin ** count
print(ans)