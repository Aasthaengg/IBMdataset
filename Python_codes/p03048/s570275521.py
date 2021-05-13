import sys

R, G, B, N = map(int, sys.stdin.readline().split())

r_max = N // R
g_max = N // G

ans = 0
for r in range(r_max+1):
    for g in range(g_max+1):
        res = N - r * R - g * G
        if 0 <= res and res % B == 0:
            # print(r, g, res // B)
            ans += 1

print(ans)