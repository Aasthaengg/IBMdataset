_ = int(input())
ax = list(map(int, input().split()))
ans = 0

for a in ax:
    i = a
    while i % 2 == 0:
        i = i//2
        ans += 1

print(ans)
