n = int(input())
l = [input() for _ in range(3)]

ans = 0
for i in range(n):
    s = set()
    for x in l:
        s.add(x[i])

    ans += len(s) - 1

print(ans)