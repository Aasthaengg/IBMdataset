
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    H, W, A, B = ZZ()
    ans = [[0] * W for _ in range(H)]
    for i in range(B):
        for j in range(A): ans[i][j] = 1
    for i in range(B, H):
        for j in range(A, W): ans[i][j] = 1
    for i in range(H): print(*ans[i], sep='')

    return

if __name__ == '__main__':
    main()
