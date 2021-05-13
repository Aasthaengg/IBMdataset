from sys import stdin
N, H, W = [int(_) for _ in stdin.readline().rstrip().split()]
AB = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
ans = 0
for a, b in AB:
    if H <= a and W <= b:
        ans += 1
print(ans)