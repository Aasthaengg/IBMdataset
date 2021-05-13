
def resolve():
    H, W, A, B = map(int, input().split())
    G = [[0] * W for _ in range(H)]

    for _ in range(B):
        print('0' * A + '1' * (W - A))
    for _ in range(H - B):
        print('1' * A + '0' * (W - A))


if __name__ == "__main__":
    resolve()