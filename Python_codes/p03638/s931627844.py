#!/usr/bin/env python3
import sys

def solve(H: int, W: int, N: int, a: "List[int]"):
    cur_index = 0
    answer_grid = [[0]*W for _ in range(H)]

    for i in range(H):
        if i%2 == 0:
            for j in range(W):
                answer_grid[i][j] = cur_index+1
                a[cur_index] -= 1
                if a[cur_index] == 0:
                    cur_index += 1

        else:
            for j in range(W-1,-1,-1):
                answer_grid[i][j] = cur_index+1
                a[cur_index] -= 1
                if a[cur_index] == 0:
                    cur_index += 1
    for i in range(H):
        print(*answer_grid[i])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(H, W, N, a)

if __name__ == '__main__':
    main()
