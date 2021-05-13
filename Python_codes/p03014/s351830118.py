import sys
import copy

input = sys.stdin.readline

def mymax(a, b, c=None):
    """
        最大値を返すメソッド.
        値が2, 3つの場合のみ対応している.
    """
    if c == None:
        if a > b:
            return a
        else:
            return b

    if a > b:
        if c > a:
            return c
        else:
            return a
    else:
        if c > b:
            return c
        else:
            return b

def main():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(input()[:-1]))
    
    L = [[0] * W for _ in range(H)]
    R = copy.deepcopy(L)
    U = copy.deepcopy(L)
    D = copy.deepcopy(L)
    
    for h in range(H):
        cntL, cntR = 0, 0
        for w in range(W):
            wreverse = W - w - 1
            if grid[h][w] == '.':
                cntL += 1
            else:
                cntL = 0
            if grid[h][wreverse] == '.':
                cntR += 1
            else:
                cntR = 0
            L[h][w] = cntL
            R[h][wreverse] = cntR

    for w in range(W):
        cntU, cntD = 0, 0
        for h in range(H):
            hreverse = H - h - 1
            if grid[h][w] == '.':
                cntU += 1
            else:
                cntU = 0
            if grid[hreverse][w] == '.':
                cntD += 1
            else:
                cntD = 0
            U[h][w] = cntU
            D[hreverse][w] = cntD
    
    ans = 0
    for h in range(H):
        for w in range(W):
            ans = mymax(ans, L[h][w] + R[h][w] + U[h][w] + D[h][w] - 3)

    print(ans)
        
if __name__ == "__main__":
    main()
