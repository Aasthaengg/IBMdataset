from sys import stdin
X, Y = [int(_) for _ in stdin.readline().rstrip().split()]
ans = max(0, 4-X) + max(0, 4-Y)
if X == Y == 1:
    print((ans + 4) * 100000)
else:
    print(ans*100000)