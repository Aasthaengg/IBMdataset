R, G, B, N = map(int, input().split())


R, G, B = sorted((R, G, B), reverse=True)

ans = 0

for i in range(N//R+1):
    for j in range((N-R*i)//G+1):
        if (N-R*i-G*j) % B == 0:
            ans += 1

print(ans)