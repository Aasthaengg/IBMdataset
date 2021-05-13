#!/usr/bin/env python3
import sys


def solve(A: int, B: int):
    # 100,100のグリッド作る
    grid = [["."]*100 for _ in range(50)]+ [["#"]*100 for _ in range(50)]
    A-=1
    B-=1

    # .を＃に置き換えていく
    for i in range(50):
        for j in range(100):
            if i%2 == 0 and j%2 == 0 and B > 0:
                grid[i][j] = "#"
                B-=1
    
    for i in range(51,100):
        for j in range(100):
            if i%2 == 0 and j%2 == 0 and A>0:
                grid[i][j] = "."
                A-=1
    
    print(100, 100)
    for i in range(100):
        print(''.join(grid[i]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
