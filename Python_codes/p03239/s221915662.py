N, T = map(int, input().split())

ans = float('inf')

for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        ans = min(ans, c)
            
if ans == float('inf'):
    print('TLE')
else:
    print(ans)