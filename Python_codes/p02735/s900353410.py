H, W = list(map(int, input().split()))
m = [list(input()) for _ in range(H)]
scores = [[None for _ in range(W)] for _ in range(H)]
def calc(i, j):
#     print(f'{i}, {j}')
    global m, scores, H, W
    if scores[i][j] is not None:
        return scores[i][j]
    if i == H - 1 and j == W - 1 and i != 0 and j != 0:
        score = 0
        scores[i][j] = score
#         print(f'i: {i}, j: {j}, score: {score}')
        return score
    diff = []
    if j < W - 1:
        diff.append((0, 1))
    if i < H - 1:
        diff.append((1, 0))
#     print(f'diff: {diff}')
    score_cand = []
    for di, dj in diff:
        additional = 0
        if (m[i][j] == '.' and m[i+di][j+dj] == '#') or (i == 0 and j == 0 and m[0][0] == '#'):
            additional += 1 
        score = calc(i+di, j+dj) + additional
        score_cand.append(score)
    score = min(score_cand)
    scores[i][j] = score
#     print(f'i: {i}, j: {j}, score: {score}')
    return score
print(calc(0, 0))