a, b, c = map(int, input().split())

M = max(a, b, c)

if (a+b+c)%2 != (M* 3) % 2:
    M += 1


diff = 3 * M - a - b - c
print(diff // 2)