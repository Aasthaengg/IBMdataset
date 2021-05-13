import sys

def solve():
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    B = []
    Ans = [[-1 for _ in range(W)] for i in range(H)]
    count = 1
    lastH = -1
    for h in range(H):
        S = input().strip("\n")
        last = -1
        for w in range(W):
            if S[w] == "#":
                last = w
        if last >= 0:
            for w in range(W):
                if S[w] == "#":
                    Ans[h][w] = count
                    for dh in B:
                        Ans[dh][w] = count
                    count += 1
                else:
                    if w < last:
                        Ans[h][w] = count
                        for dh in B: Ans[dh][w] = count
                    else:
                        Ans[h][w] = count - 1
                        for dh in B: Ans[dh][w] = count - 1
            B.clear()
            lastH = h
        else:
            B.append(h)
    if len(B) > 0:
        for h in B:
            for w in range(W):
                Ans[h][w] = Ans[lastH][w]

    for h in range(H):
        print(*Ans[h], sep=" ")

    return 0

if __name__ == "__main__":
    solve()