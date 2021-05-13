def main():
    import sys
    input = sys.stdin.buffer.readline
    H, W = (int(i) for i in input().split())
    A = [[int(i) for i in input().split()] for j in range(H)]
    ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 1:
                if w != W-1:
                    A[h][w] -= 1
                    A[h][w+1] += 1
                    ans.append((h+1, w+1, h+1, w+2))
                elif h != H-1:
                    A[h][w] -= 1
                    A[h+1][w] += 1
                    ans.append((h+1, w+1, h+2, w+1))

    print(len(ans))
    for a in ans:
        print(*a)


if __name__ == '__main__':
    main()
