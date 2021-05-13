n = int(input())

ans = 0
for i in range(n):
    l = list(map(int,input().split()))
    ans += max(l)-min(l)+1

print(ans)