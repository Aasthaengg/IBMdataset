n = int(input())
a = sorted(map(int, input().split()), reverse=True)
total = sum(a)

ans = 1
for x in a:
    total -= x
    if x > total * 2:
        break
    ans += 1

print(ans)