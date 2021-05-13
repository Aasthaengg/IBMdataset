n = int(input())
LR = [list(map(int, input().split())) for _ in range(n)]
ans = [r - l + 1 for (l, r) in LR]
print(sum(ans))