R, G, B, N = map(int, input().split())

ans = 0
for r in range(N//R+1):
    for g in range((N-r*R)//G+1):
        tmp = (N-r*R-g*G)/B
        if tmp.is_integer():
            ans += 1

print(ans)