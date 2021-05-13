A, B = map(int, input().split())

ans = 0

for i in range(1, 9 + 1):
    for j in range(10):
        for k in range(10):
            i, j, k = str(i), str(j), str(k)
            kaibun = int(i+j+k+j+i)
            if A <= kaibun and kaibun <= B:
                ans += 1

print(ans)