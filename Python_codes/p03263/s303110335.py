import sys

def solve():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A = [[int(a) for a in input().split()] for _ in range(H)]
    Ans = []
    for n in range(H * W - 1):
        h, w = n // W, n % W
        if A[h][w] % 2 == 1:
            if w < W - 1:
                Ans.append((h+1, w+1, h+1, w+2))
                A[h][w] -= 1
                A[h][w+1] += 1
            else:
                Ans.append((h+1, w+1, h+2, w+1))
                A[h][w] -= 1
                A[h+1][w] += 1
    print(len(Ans))
    for move in Ans:
        print(" ".join(map(str, move)))
   
    return 0

if __name__ == "__main__":
    solve()