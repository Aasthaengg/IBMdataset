n, k = map(int, input().split())
l = []
ans = 0

for i in range(1,n+1):
    for j in range(20):
        if 2**j >= k/i:
            l.append(j)
            break

for i in l:
    ans += 1/n * (1/2)**i
print(ans)