n = int(input())
seats = [list(map(int, input().split())) for _ in range(n)]

nop = [s[-1] - s[0] + 1 for s in seats]
r = sum(nop)

print(r)
