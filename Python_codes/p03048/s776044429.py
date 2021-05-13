R, G, B, N = map(int, input().split())
R_max = N // R + 1
G_max = N // G + 1
B_max = N // B + 1
ans = 0
for i in range(0, R_max):
    for j in range(0, G_max):
        #for k in range(0, B_max):
            #if i * R + j * G + k * B == N:
        #a, b = divmod(N - (i * R + j * G), B)
        if (N - (i * R + j * G)) % B == 0 and (N - (i * R + j * G)) >= 0:
            #print('ans', i, j)
            ans += 1
print(ans)
