H, W = map(int, input().split())
a, b = [], []
ans = 0
for _ in range(H):
    a += [0 if x == '.' else 1 for x in input()]
for i in range(H*W):
    if a[i] == 0:
        if i % W != 0: ans += a[i-1]
        if (i+1) % W != 0: ans += a[i+1]
        if i < (H-1)*W: ans += a[i+W]
        if i < (H-1)*W and i % W != 0: ans += a[i+W-1]
        if i < (H-1)*W and (i+1) % W != 0: ans += a[i+W+1]
        if W <= i: ans += a[i-W]
        if i % W != 0 and W <= i: ans += a[i-W-1]
        if W <= i and (i+1) % W != 0: ans += a[i-W+1]
        b += [str(ans)]
        ans = 0
    else:
        b += ['#']
        
for i in range(H):
    print(''.join(b[W*i:W*(i+1)]))

