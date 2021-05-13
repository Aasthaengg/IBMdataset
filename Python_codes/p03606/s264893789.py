N = int(input())

ans = 0
for _ in range(N):
    x,y = map(int,input().split())
    ans += abs(x-y) + 1
print(ans)