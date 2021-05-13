R, G, B, N = map(int, input().split())

ans = 0
for i in range(3001):
    for j in range(3001):
        b = (N-i*R-j*G)/B
        if b.is_integer() and b >= 0:
            ans += 1
        if b < 0:
            break

print(ans)