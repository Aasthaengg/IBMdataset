n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    while i % 32 == 0:
        i //= 32
        ans += 5
    while i % 2 == 0:
        i //= 2
        ans += 1

print(ans)