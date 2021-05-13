n = int(input())
lis = list(map(int, input().split()))

lis = sorted(lis, reverse=True)

ans = 0
for i in range(1,n):
    ans += lis[i//2]
        

print(ans)