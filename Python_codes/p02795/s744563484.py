H = int(input())
W = int(input())
N = int(input())

if H < W:
    H, W = W, H

ans = 0
while N > 0:
    N -= H
    ans += 1

print(ans)