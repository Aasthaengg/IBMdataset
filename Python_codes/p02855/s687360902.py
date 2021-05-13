import sys
from copy import deepcopy
def input(): return sys.stdin.readline().strip()

def main():
    H, W, K = map(int, input().split())
    cake = [input() for _ in range(H)]
    ans_cake = [[0]* W for _ in range(H)]

    row_num = [raw.count("#") for raw in cake]

    top_row = min([i for i, num in enumerate(row_num) if num != 0])
    
    cake_idx = 0
    for i, (cake_row, num) in enumerate(zip(cake[top_row:], row_num[top_row:])):
        i += top_row
        if num:
            cake_idx += 1
            for j in range(W):
                ans_cake[i][j] = cake_idx
                if cake_row[j] == "#":
                    num -= 1
                    if num:
                        cake_idx += 1
        else:
            ans_cake[i] = deepcopy(ans_cake[i-1])

    for i in range(top_row):
        ans_cake[i] = deepcopy(ans_cake[top_row])
    
    for ans_cake_row in ans_cake:
        print(*ans_cake_row, sep=" ")




if __name__ == "__main__":
    main()