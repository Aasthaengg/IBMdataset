n, x = map(int, input().split())
aa = list(map(int, input().split()))

moves = 0
if aa[0] > x:
    moves += aa[0] - x
    aa[0] = x

for i in range(n-1):
    # invariant: aa[i] <= x
    if aa[i] + aa[i+1] > x:
        diff = (aa[i] + aa[i+1]) - x
        aa[i+1] -= diff
        moves += diff

print(moves)
