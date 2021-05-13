N, K = [int(_) for _ in input().split()]

scores = []
max_patterns = 0

for dice in range(1, N + 1):
    score = dice
    coin_counts = 0
    while score < K:
        score *= 2
        coin_counts += 1
    patterns = 2 ** coin_counts
    max_patterns = max(patterns, max_patterns)
    lose = patterns - 1
    win = 1
    scores.append((win, lose, patterns))

total_win = 0
total_lose = 0
for win, lose, patterns in scores:
    ratio = max_patterns // patterns
    total_win += win * ratio
    total_lose += lose * ratio

win_ratio = total_win / (total_win + total_lose)
print(win_ratio)
