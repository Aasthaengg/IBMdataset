def check_adjacents(S, i, j):
    return i > 0 and S[i-1][j] == '#' or \
           i < H - 1 and S[i+1][j] == '#' or \
           j > 0 and S[i][j-1] == '#' or \
           j < W - 1 and S[i][j+1] == '#'

def solution(H, W, S):
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                adjacents_sharp = check_adjacents(S, i, j)
                if not adjacents_sharp:
                    return 'No'
    return 'Yes'

H, W = map(int, input().split())
S = [input() for _ in range(H)]
print(solution(H, W, S))