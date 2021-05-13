n, c = map(int, input().split())
sushi = [tuple(map(int, input().split())) for _ in range(n)]
sushi = [(0, 0)] + sushi
cclkmax = [0] * (n+1)
cumvalue = 0
for i in range(1, n+1):
    cumvalue += sushi[i][1]
    cclkmax[i] = max(cclkmax[i-1], cumvalue - sushi[i][0])
maxscore = cclkmax[n]
cum = 0
for i in range(n, 0, -1):
    cum += sushi[i][1]
    score = cclkmax[i-1] + cum - 2*(c - sushi[i][0])
    maxscore = max(maxscore, score)
clkmax = [0] * (n+1)
cumvalue = 0
for i in range(n, 0, -1):
    cumvalue += sushi[i][1]
    clkmax[i] = max(clkmax[(i+1)%(n+1)], cumvalue - (c - sushi[i][0]))
maxscore = max(maxscore, clkmax[1])
cum = 0
for i in range(1, n+1):
    cum += sushi[i][1]
    score = clkmax[(i+1)%(n+1)] + cum - 2*sushi[i][0]
    maxscore = max(maxscore, score)
print(maxscore)