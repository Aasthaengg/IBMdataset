R, G, B, N = map(int, input().split())

ans = 0
for r in range(3001):
    for g in range(3001):
        tmp = (R*r+G*g)
        if tmp > N:
            break

        if (N-tmp) % B == 0 or tmp == N:
            ans += 1
print(ans)
