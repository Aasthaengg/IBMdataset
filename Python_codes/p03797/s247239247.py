import sys
input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
c_2 = M //2
if c_2 <= N:
    print(min(N, c_2))
    sys.exit()
ans = N
M -= 2 * N
ans += M //4
print(ans)