R, G, B, N = map(int, input().split())
ans = 0
i = 0
while R*i <=  N:
    j = 0
    while R*i + G*j <=  N:
        if (N - R*i - G*j) % B ==  0:
            ans += 1
        j += 1
    i += 1
print(ans)
