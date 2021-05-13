N = int(input())

A = list(map(int, input().split()))

ans = 1

for item in A:
    ans *= item

    ans = min(ans, 10**18 + 1)

if ans == 10**18 + 1:
    print(-1)
    exit()

print(ans)