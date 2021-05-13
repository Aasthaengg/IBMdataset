N, T = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(N)]
ct = sorted(ct, key=lambda x:x[1])
mx = float('inf')

for c, t in ct:
    if t <= T:
        mx = min(mx, c)

if mx != float('inf'):
    print(mx)
    exit()
print('TLE')
