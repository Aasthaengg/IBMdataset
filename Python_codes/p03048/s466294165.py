R, G, B, N = map(int, input().split())
a = [max(1, N//R), max(1, N//G)]
ans = 0
for i in range(0, a[0]+1):
    for j in range(0, a[1]+1):
        if i*R+j*G > N:
            break
        elif (N-i*R-j*G) % B == 0:
            ans += 1
print(ans)
