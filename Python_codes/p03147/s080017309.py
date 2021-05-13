n = int(input())

lis = list(map(int, input().split()))

ans = lis[0]

for i in range(n-1):
    if lis[i] < lis[i+1]:
        ans += lis[i+1] - lis[i]
        
print(ans)