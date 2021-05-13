H, W, K = [int(x) for x in input().split()]

C = []
for i in range(H):
    C.append(input())

ans = 0
for h in range(2 ** H, 2 ** H + 2 ** H):
    bin_h = format(h, 'b')[1:]
    for w in range(2 ** W, 2 ** W + 2 ** W):
        bin_w = format(w, 'b')[1:]
        count = 0
        for i in range(H):
            for j in range(W):
                if bin_h[i] == '0' and bin_w[j] == '0' and C[i][j] == '#':
                    count += 1
        if count == K:
            ans += 1

print(ans)