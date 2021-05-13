n = int(input())
stones = input()
white = stones.count('.')
black = 0
ans = white
for c in stones:
    if c == '#':
        black += 1
    else:
        white -= 1
    score = black + white
    ans = min(score, ans)
print(ans)