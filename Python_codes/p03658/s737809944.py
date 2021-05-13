n, k = map(int, input().split())
lis = list(map(int, input().split()))

lis = sorted(lis, reverse = True)

ans = 0
for i in range(k):
    ans += lis[i]
    
print(ans)