N = int(input())

ans = -1

for i in range(N+1):
    ans += len(str(i))%2 > 0

print(ans)