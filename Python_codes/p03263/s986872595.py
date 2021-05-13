import sys

def solve():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A = [[int(a) for a in input().split()] for _ in range(H)]
    Ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 1:
                if w < W - 1:
                    A[h][w] -= 1
                    A[h][w+1] += 1
                    Ans.append((h+1, w+1, h+1, w+2))
                else:
                    if h < H - 1:
                        A[h][w] -= 1
                        A[h+1][w] += 1
                        Ans.append((h+1, w+1, h+2, w+1))
    count = len(Ans)
    print(count)
    for i in range(count):
        print(*Ans[i], sep=" ")
    

    return 0

if __name__ == "__main__":
    solve()