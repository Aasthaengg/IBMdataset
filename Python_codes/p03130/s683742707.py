d = {i: 0 for i in range(1, 5)}
for i in range(3):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1

ans = 'YES'
for i in d.values():
    if i == 3:
        ans = 'NO'
        break

print(ans)

