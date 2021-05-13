# abc085

N, Y = map(int, input().split())
ans = "-1 -1 -1"

for x in range(N + 1):
    for y in range(N - x + 1):
        z = N - x - y
        if x*10000 + y*5000 + z*1000 == Y:
            ans = (" ".join(list(map(str, [x, y, z]))))
            break

print(ans)